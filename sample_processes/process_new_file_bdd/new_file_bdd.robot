*** Settings ***
Library                         RobotProcessLibrary


*** Keywords ***
check if ${file_name} is not in this folder
    File Should Not Exist       ${file_name}

create a file with name ${file_name} in this folder
    Create New File             ${file_name}

check if ${file_name} exists
    File Should Exist           ${file_name}


*** Processes ***
Creating file.txt                                    
    Given check if file.txt is not in this folder
    When create a file with name file.txt in this folder
    Then check if file.txt exists
