from pdf2image import convert_from_path

images = convert_from_path("/home/qiming/Desktop/code/project_pages/RevisitOVS/static/images/first_page.pdf", dpi=300)

# 保存为高质量 JPG 或 PNG
images[0].save("/home/qiming/Desktop/code/project_pages/RevisitOVS/static/images/first_page.png", "PNG", quality=95)