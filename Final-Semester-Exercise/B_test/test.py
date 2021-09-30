import re


class CleanData:

    def extractDialogue(self):
        """
        A function that extract dialogue lines from the original script file and remove all other meta-data
        Returns:
            1.list: A list of clean-up character names and dilogues
        """
        file = open("input_script.txt", 'r')
        data = file.read()

        delete_bracket = re.sub(r"\(.*?\)|\[.*?\]", "", data)   # Delete all sentences that contain(),[]

        delete_space = re.sub(r'[^\S\r\n]{2,}', " ", delete_bracket)    # Remove the spaces after the parenthesis

        delete_by = re.sub(r".*by:.*", "", delete_space)    # Delete the sentence with the beginning: by

        delete_empty_rows = "".join([s for s in delete_by.splitlines(True) if s.strip()])   # Delete all empty rows

        separate_input = delete_empty_rows.split('\n')    # Separate them in the form of line breaks

        for line in separate_input:
            if re.search(r"^((?!:).)*$", line) != None:     # Delete all sentences without colon
                separate_input.remove(line)


        clean_dialogue = []
        for i in range(len(separate_input)):      # Separate lists into character names, and their dialogues.
            clean_line = separate_input[i].split(": ")      # Delete the space after the colon
            clean_dialogue.append(tuple(clean_line))    # covert list to tuple

        return clean_dialogue

    #Put the extracted text in a new file
    def saveDialogue(self):

        dialogue = self.extractDialogue()

        with open('test_clean_dialogue.txt', 'w') as f:
            f.write(str(dialogue))




clean_data = CleanData()
clean_data.saveDialogue()