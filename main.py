from selenium import webdriver
from selenium.webdriver.common.keys import Keys


#clicks = input("How many clicks do you want:    ")
clicks = "50000"

driver = webdriver.Chrome()
driver.get("https://popcat.click")

elem = driver.find_element_by_tag_name('body')

clicks2 = 0
while(int(clicks) > clicks2):
    clicks2 = clicks2 + 1
    print("click: " + str(clicks2 * 500))
    elem.send_keys("""afCDDD0zoMRGJmeOuiB6v2worCXYDRYcR9y91MqRiEpL5rC3tiGguhwmMTDxLp065RH8Re9aXvvjxD4xaLS7eC8lV1cwmLYTF6rhsKMfNV50GFvAUppYkMZsz8PqvZkPxbiatJgbcnCWOeJZnaDfeeVJFp2qDnPBme0jEVmBuCQaQp2RyLEEYElNLj1PQ68HzejGdztvYpNchsKjXzxAbHXVPbU6dYxE9ZZ8llzvWlumxS22fHKJ4aZzR44QZxgBCVfcrb4i7Z21qsSeeBgPC9QDihaipvWHqPTiQGNkKzrxM8ANeSJGFu2Qw9xi9AnDCo6an47ddU6bBr2Rgl2F3rwUK2ySOPuk4nvJraQROOMekfHrjfoAG01Sl5H1oPNH8jlZaa8hG6S1XJNRxCFeboq3JJucuWaMRjX9wvji5jsQSqymOBgEqmjFfSzTjI7zU7Vv95DFpmdN1TLtWP3kzYh0OEB6JDxLggC9Vrp9RXV7lu5PPPwQ""")

print(clicks + " sent")