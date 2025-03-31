import os
from pdf2image import convert_from_path

# 配置项
pdf_path = '/home/qiming/Desktop/code/project_pages/RevisitOVS/static/CD.pdf'  # 替换为你的PDF路径
output_folder = './'  # 输出图片文件夹
dpi = 300  # 分辨率 DPI 设置（越高越清晰）

# 创建输出文件夹（如果不存在）
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 将 PDF 转换为图像
print(f"正在将 {pdf_path} 转换为 PNG 图片...")
images = convert_from_path(pdf_path, dpi=dpi)

# 保存每一页为 PNG
for i, img in enumerate(images):
    image_path = os.path.join(output_folder, f'page_{i+1:03}.png')
    img.save(image_path, 'PNG')
    print(f"已保存: {image_path}")

print("转换完成！")
