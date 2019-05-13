*** Settings ***
Library                         RobotProcessLibrary


*** Keywords ***
Create And Check                                     # új keyword készítése
    [Arguments]                 ${file_name}

    Create New File             ${file_name}
    File Should Exist           ${file_name}


*** Processes ***
Creating file.txt                                    
    File Should Not Exist       file.txt
    Create And Check            file.txt
