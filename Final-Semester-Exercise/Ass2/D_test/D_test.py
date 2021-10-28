import re
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


class CleanData:
    """
    This class is used to clean data
    """

    def extractDialogue(self):
        """
        A function that extract dialogue lines from the original script file and remove all other meta-data
        Returns:
            1.list: A list of clean-up character names and dilogues
        """
        input_file = open("input_script.txt", 'r')
        input_data = input_file.read()

        delete_bracket = re.sub(r"\(.*?\)|\[.*?\]", "", input_data)  # Delete all sentences that contain(),[]

        delete_space = re.sub(r'[^\S\r\n]{2,}', " ", delete_bracket)  # Remove the spaces after the parenthesis

        delete_by = re.sub(r".*by:.*", "", delete_space)  # Delete the sentence with the beginning: by

        delete_empty_rows = "".join([s for s in delete_by.splitlines(True) if s.strip()])  # Delete all empty rows

        separate_input = delete_empty_rows.split('\n')  # Separate them in the form of line breaks

        for line in separate_input:
            if re.search(r"^((?!:).)*$", line) != None:  # Delete all sentences without colon
                separate_input.remove(line)

        clean_dialogue = []
        for i in range(len(separate_input)):  # Separate lists into character names, and their dialogues.
            clean_line = separate_input[i].split(": ")  # Delete the space after the colon
            clean_dialogue.append(tuple(clean_line))  # covert list to tuple

        return clean_dialogue

    def saveExtractDialogue(self):
        """
        A function that put the extracted text in a new file
        """
        extract_dialogue = self.extractDialogue()

        with open('32009682_clean_dialogue.txt', 'w') as f:
            f.write(str(extract_dialogue))

    def separateDialogue(self):
        """
        A function that separate the dialogues of different characters(roles)
         Return:
            1.dictionary: A dictionary to tore dialogue together according to the role
        """
        clean_dialogue_file = open('32009682_clean_dialogue.txt', 'r')

        clean_dialogue_data = clean_dialogue_file.read()

        clean_dialogue_list = eval(clean_dialogue_data)  # Converts the String read out by the file to the List

        separate_dialogue = {}  # Bring together dialogue under one character

        for line in clean_dialogue_list:
            if line[0] in separate_dialogue.keys():
                separate_dialogue[line[0]] += (line[1] + '\n')
            else:
                separate_dialogue[line[0]] = (line[1] + '\n')

        # Write the dialogues of the corresponding role to its file
        for role in separate_dialogue:
            with open('32009682_' + role.lower() + '.txt', 'w') as f:
                f.write(str(separate_dialogue[role]))
        return separate_dialogue


class AnalyzeData:
    """
    This class is used to analyze data
    """

    def obtainFrequentWords(self):
        """
        A function that obtain Top 5 Frequent Words For Each Role
        Return:
            1.dataframe: A dataframe to store the information of role,word,and freq:
        """

        clean_data = CleanData()
        clean_data.saveExtractDialogue()  # Call the method of the CleanData class
        separate_dialogue = clean_data.separateDialogue()

        holding = {}  # Because dataframe needs to be merged at the end, all holding data frames are stored using holding{}

        for role in separate_dialogue:
            separate_file = open('32009682_' + role.lower() + '.txt', 'r')

            separate_data = separate_file.read()

            delete_line_break = separate_data.replace("\n", "")  # Remove the line break

            separate_word = delete_line_break.split(' ')  # Separate words according to space

            unique_word = set(separate_word)  # Find words that don't repeat in a role

            if len(unique_word) > 100:  # Select a character with a number of unique words greater than 100

                lower_data = separate_data.lower()  # Case insensitive, so all data is replaced with lowercase

                separate_lower_data = lower_data.split("\n")

                separate_word = []  # The row frequency is obtained when each row is calculated together to remove the duplicate elements

                for i in separate_lower_data[:-1]:  # Because the last line is \n , so don't read it specifically

                    list_dialogue = i.strip().split(" ")  # Delete the spaces at the end of each line

                    new_set = set(list_dialogue)  # Remove the duplicate elements from each row
                    separate_word += new_set

                word_counter = Counter(separate_word)  # Calculate the number of words that appear for each word

                highest_frequencies = word_counter.most_common(5)  # The top 5 with the highest frequency

                df = pd.DataFrame(highest_frequencies, columns=['word', 'freq'])  # Store the data to dataframe

                df.insert(0, 'role', role.lower())  # Insert this column of the role into the first column

                holding[role] = df  # Store all hold data frames

        df_data = pd.concat(list(holding.values()), ignore_index=True)  # merged dataframe

        df_data.to_csv('32009682_data.csv')

        return df_data

    def visualiseData(self):
        """
        Visualise the DataFrame with a graph.
        """
        analze_data = AnalyzeData()
        df_data = analze_data.obtainFrequentWords()

        np_data = np.array(df_data)
        np_data = np_data.tolist()
        role = []
        for i in np_data:
            role.append(i[0])

        if len(role) == 30:
            # Set the title and x,y axis to the first role
            first_role = df_data.iloc[0, 0]
            first_role_words = df_data.iloc[0:5, 1:2]
            first_role_x = np.array(first_role_words)      # Convert dataframe to np.array
            first_role_x = np.squeeze(first_role_x)       # Remove redundant dimensions
            first_role_freq = df_data.iloc[0:5, 2:3]
            first_role_y = np.array(first_role_freq)
            first_role_y = np.squeeze(first_role_y)
            first_role_y = first_role_y.astype(int)   # The internal type is converted to int

            # Set the title and x,y axis to the second role
            second_role = df_data.iloc[5, 0]
            second_role_words = df_data.iloc[5:10, 1:2]
            second_role_x = np.array(second_role_words)
            second_role_x = np.squeeze(second_role_x)
            second_role_freq = df_data.iloc[5:10, 2:3]
            second_role_y = np.array(second_role_freq)
            second_role_y = np.squeeze(second_role_y)
            second_role_y = second_role_y.astype(int)

            # Set the title and x,y axis to the third role
            third_role = df_data.iloc[10, 0]
            third_role_words = df_data.iloc[10:15, 1:2]
            third_role_x = np.array(third_role_words)
            third_role_x = np.squeeze(third_role_x)
            third_role_freq = df_data.iloc[10:15, 2:3]
            third_role_y = np.array(third_role_freq)
            third_role_y = np.squeeze(third_role_y)
            third_role_y = third_role_y.astype(int)

            fourth_role = df_data.iloc[15, 0]
            fourth_role_words = df_data.iloc[15:20, 1:2]
            fourth_role_x = np.array(fourth_role_words)
            fourth_role_x = np.squeeze(fourth_role_x)
            fourth_role_freq = df_data.iloc[15:20, 2:3]
            fourth_role_y = np.array(fourth_role_freq)
            fourth_role_y = np.squeeze(fourth_role_y)
            fourth_role_y = fourth_role_y.astype(int)

            fifth_role = df_data.iloc[20, 0]
            fifth_role_words = df_data.iloc[20:25, 1:2]
            fifth_role_x = np.array(fifth_role_words)
            fifth_role_x = np.squeeze(fifth_role_x)
            fifth_role_freq = df_data.iloc[20:25, 2:3]
            fifth_role_y = np.array(fifth_role_freq)
            fifth_role_y = np.squeeze(fifth_role_y)
            fifth_role_y = fifth_role_y.astype(int)

            sixth_role = df_data.iloc[25, 0]
            sixth_role_words = df_data.iloc[25:30, 1:2]
            sixth_role_x = np.array(sixth_role_words)
            sixth_role_x = np.squeeze(sixth_role_x)
            sixth_role_freq = df_data.iloc[25:30, 2:3]
            sixth_role_y = np.array(sixth_role_freq)
            sixth_role_y = np.squeeze(sixth_role_y)
            sixth_role_y = sixth_role_y.astype(int)


            fig = plt.figure()  # Draw the figure

            ax = fig.add_subplot(111)  # The big subplot
            ax1 = fig.add_subplot(231)  # Draw a subplot
            ax2 = fig.add_subplot(232)
            ax3 = fig.add_subplot(233)
            ax4 = fig.add_subplot(234)
            ax5 = fig.add_subplot(235)
            ax6 = fig.add_subplot(236)

            ax1.bar(first_role_x, first_role_y)     # Set the x,y axis to the subplot
            ax1.set_title(first_role)   # Set the title to the subplot

            ax2.bar(second_role_x, second_role_y)
            ax2.set_title(second_role)

            ax3.bar(third_role_x, third_role_y)
            ax3.set_title(third_role)

            ax4.bar(fourth_role_x, fourth_role_y)
            ax4.set_title(fourth_role)

            ax5.bar(fifth_role_x, fifth_role_y)
            ax5.set_title(fifth_role)

            ax6.bar(sixth_role_x, sixth_role_y)
            ax6.set_title(sixth_role)

            fig.tight_layout()  # Adjust the overall white space

            # Turn off axis lines and ticks of the big subplot
            ax.spines['top'].set_color('none')
            ax.spines['bottom'].set_color('none')
            ax.spines['left'].set_color('none')
            ax.spines['right'].set_color('none')
            ax.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')

            # set the x,y axis to the big subplot
            ax.set_xlabel('word', fontsize=20)
            ax.set_ylabel('freq', fontsize=20)

            plt.show()  # show graph
        else:
            df_data.plot(x='word', kind='bar')
            plt.show()

# Create an instance of AnalyzeData class and call the visualiseData method of that instance, and then the program will run automatically
analze_data = AnalyzeData()
analze_data.visualiseData()