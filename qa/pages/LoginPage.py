from qa.pages.BasePage import Actions


class LoginLoc(Actions):
    email = ":r1:"
    password = ":r2:"
    login_button = "//button[@data-testid='login-button']"
    chargebacks = "//span[text() = '3P Chargebacks']"
    length_xpath = '//tr[@class="MuiTableRow-root css-1un8s7z-MuiTableRow-root"][1]//td[@class="MuiTableCell-root MuiTableCell-body MuiTableCell-sizeMedium css-w25kid-MuiTableCell-root"]'
    base_xpath = '//tbody[@class="MuiTableBody-root css-apqrd9-MuiTableBody-root"]//tr[@class="MuiTableRow-root css-1u3yjyd-MuiTableRow-root" or @class="MuiTableRow-root css-1un8s7z-MuiTableRow-root"]//td[@class="MuiTableCell-root MuiTableCell-body MuiTableCell-sizeMedium css-w25kid-MuiTableCell-root"][{}]'
    history_by_store = "//div[@class='MuiCollapse-root MuiCollapse-vertical MuiCollapse-entered css-c4sutr']//span[text()='History by Store']"
    rows = '//tr[@class="MuiTableRow-root css-1un8s7z-MuiTableRow-root"][1]//td[@class="MuiTableCell-root MuiTableCell-body MuiTableCell-sizeMedium css-w25kid-MuiTableCell-root"]'
    values_xpath = '//tbody[@class="MuiTableBody-root css-apqrd9-MuiTableBody-root"]//tr[@class="MuiTableRow-root css-1u3yjyd-MuiTableRow-root" or @class="MuiTableRow-root css-1un8s7z-MuiTableRow-root"]//td[@class="MuiTableCell-root MuiTableCell-body MuiTableCell-sizeMedium css-w25kid-MuiTableCell-root"][{}]'
    next_button = '//button[@type="button" and @data-testid="pagination-next"]'
    previous_button = '//button[@type="button" and @data-testid="pagination-prev"]'
    transactions = '//div[@class="MuiCollapse-root MuiCollapse-vertical MuiCollapse-entered css-c4sutr"]//a[2]'
    location = '//button[@class="MuiButtonBase-root MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeLarge MuiButton-textSizeLarge MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeLarge MuiButton-textSizeLarge css-y1p833-MuiButtonBase-root-MuiButton-root"][1]'
    clear = "//button[@type='button' and text()='Clear']"
    alchemy = '//p[@class="MuiTypography-root MuiTypography-body1 MuiTypography-noWrap css-1va4yrs-MuiTypography-root" and text()="Artisan Alchemy"]'
    buffet = '//p[@class="MuiTypography-root MuiTypography-body1 MuiTypography-noWrap css-1va4yrs-MuiTypography-root" and text()="Blissful Buffet"]'
    apply = '// button[@class ="MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeSmall MuiButton-containedSizeSmall MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeSmall MuiButton-containedSizeSmall css-1un93pa-MuiButtonBase-root-MuiButton-root" and @ data-testid="applyBtn"]'
    market_place = '//button[@class="MuiButtonBase-root MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeLarge MuiButton-textSizeLarge MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeLarge MuiButton-textSizeLarge css-y1p833-MuiButtonBase-root-MuiButton-root"][3]'
    grab_hub = '//div[@class="MuiBox-root css-lg86aj"]//p[@class="MuiTypography-root MuiTypography-body1 MuiTypography-noWrap css-1va4yrs-MuiTypography-root" and text() = "Grubhub"] '
    apply_button = '//button[@data-testid="applyBtn"]'