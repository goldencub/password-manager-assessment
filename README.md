# password-manager-assessment
ICTPRG302 - Assessment 2 Password Manager 
# Pseudocode

SET FILE_NAME to "digicore_credentials.txt"

DEFINE function encrypt(text)
    SET result to empty string
    FOR each character in text
        ADD character with ASCII code + 3 to result
    RETURN result

DEFINE function decrypt(text)
    SET result to empty string
    FOR each character in text
        ADD character with ASCII code - 3 to result
    RETURN result

DEFINE function ensure_storage_file()
    IF FILE_NAME does not exist
        CREATE empty text file with that name

DEFINE function display_menu()
    PRINT program title and menu options 1–4

DEFINE function add_credentials()
    ASK user for site / resource name
    ASK user for username
    ASK user for password
    ENCRYPT each value
    OPEN file in append mode
    WRITE encrypted site, username, password separated by "|"
    CLOSE file
    PRINT confirmation message

DEFINE function retrieve_credentials()
    ASK user for site name to search for
    SET found flag to false
    OPEN file in read mode
    FOR each line in file
        STRIP newline, SPLIT line by "|"
        DECRYPT site, username, password
        IF site matches user search (ignore case)
            PRINT decrypted credentials
            SET found flag to true
            STOP loop
    IF found flag is false
        PRINT "no credentials found"

DEFINE function list_all_credentials()
    OPEN file in read mode
    READ all lines into a list
    IF list is empty
        PRINT "no entries stored yet"
    ELSE
        FOR each line with index
            STRIP newline, SPLIT by "|"
            DECRYPT site, username, password
            PRINT entry number and credential details

MAIN PROGRAM
    CALL ensure_storage_file()
    SET choice to empty string
    WHILE True
        CALL display_menu()
        ASK user for choice
        IF choice is "1"
            CALL add_credentials()
        ELSE IF choice is "2"
            CALL retrieve_credentials()
        ELSE IF choice is "3"
            CALL list_all_credentials()
        ELSE IF choice is "4"
            PRINT exit message
            BREAK out of loop
        ELSE
            PRINT "invalid option"
END PROGRAM

