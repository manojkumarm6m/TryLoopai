from qa.pages.BasePage import Actions


class Reversal(Actions):
    chargebacks = "//span[text() = '3P Chargebacks']"
    history_by_store = "//div[@class='MuiCollapse-root MuiCollapse-vertical MuiCollapse-entered css-c4sutr']//span[text()='History by Store']"
    rows = '//tr[@class="MuiTableRow-root css-1un8s7z-MuiTableRow-root"][1]//td[@class="MuiTableCell-root MuiTableCell-body MuiTableCell-sizeMedium css-w25kid-MuiTableCell-root"]'

    values_xpath = '//tbody[@class="MuiTableBody-root css-apqrd9-MuiTableBody-root"]//tr[@class="MuiTableRow-root css-1u3yjyd-MuiTableRow-root" or @class="MuiTableRow-root css-1un8s7z-MuiTableRow-root"]//td[@class="MuiTableCell-root MuiTableCell-body MuiTableCell-sizeMedium css-w25kid-MuiTableCell-root"][{}]'
