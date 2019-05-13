*** Settings ***
Library                         RobotProcessLibrary  # a szükséges importok


*** Processes ***
Creating file.txt                                    # az alfolyamat neve
    File Should Not Exist       file.txt             # keyword és paraméter
    Create New File             file.txt
    File Should Exist           file.txt
