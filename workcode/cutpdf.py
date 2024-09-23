import PyPDF2

pdf_file = open('Example1.pdf', 'rb')  #PDF名称
pdf_reader = PyPDF2.PdfReader(pdf_file)

# 拆分前四页
pdf_writer = PyPDF2.PdfWriter()
for page_num in range(4):  #选择页数
    pdf_writer.add_page(pdf_reader.pages[page_num])
output_filename = 'pages_1_to_4.pdf'
with open(output_filename, 'wb') as output:
    pdf_writer.write(output)

# 拆分5-7页
pdf_writer = PyPDF2.PdfWriter()
for page_num in range(4, 7):  #选择页数
    pdf_writer.add_page(pdf_reader.pages[page_num])
output_filename = 'pages_5_to_7.pdf'
with open(output_filename, 'wb') as output:
    pdf_writer.write(output)
