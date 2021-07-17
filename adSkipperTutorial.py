import pyautogui


def findAndClick():
    while True:
        videoAdCords = pyautogui.locateCenterOnScreen("play.png")
        bannerCords = pyautogui.locateCenterOnScreen("bannerad.png")
        blackBannerCords = pyautogui.locateCenterOnScreen("black banner.png")
        print(videoAdCords)
        print(bannerCords)
        print(blackBannerCords)

        if videoAdCords or bannerCords or blackBannerCords is not None:
            break

    if videoAdCords is not None:
        pyautogui.click(videoAdCords)
    elif bannerCords is not None:
        pyautogui.click(bannerCords)
    elif blackBannerCords is not None:
        pyautogui.click(blackBannerCords)

    findAndClick()


findAndClick()
