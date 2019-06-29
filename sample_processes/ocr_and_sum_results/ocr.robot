*** Settings ***
Library                    RobotProcessLibrary

*** Processes ***
Ocr And Sum Results

    ${szamok}=            Ocr Image  szamok.png

    Open Workbook         szamok.xlsx
    Set Active Worksheet  numbers
    Set Cell Value        A1   numbers:
    Set Cell Background   A1  E08F9D
    Add List To Column    A2  ${szamok.split(" ")}  cell_type=number
    ${empty_cell}=        Get First Empty Cell Below  A2
    ${osszeg_title}=      Get Cell Below  ${empty_cell}
    Set Cell Background   ${osszeg_title}  E08F9D
    Set Cell Value        ${osszeg_title}   sum:
    ${osszeg_cell}=       Get Cell Below  ${osszeg_title}
    Add Formula To Cell   ${osszeg_cell}   =SUM(A2:${empty_cell})
    ${result}=            Get Cell Value  ${osszeg_cell}
    Close Workbook
