from docx import Document
from docxtpl import DocxTemplate, InlineImage
import os
from docx.shared import Mm


def create_docx_handler(docx_path, need_handler=''):
    if need_handler == 'python-docx':
        document_handler = Document(docx_path)
        document_template_handler = None
    elif need_handler == 'python-docx-template':
        document_handler = None
        document_template_handler = DocxTemplate(docx_path)
    else:
        document_handler = Document(docx_path)
        document_template_handler = DocxTemplate(docx_path)
    return document_handler, document_template_handler


def write(document_template_handler, signature_img: list, signature_img_path: str, save_path: str, img_height=9):
    context = {}
    for img in signature_img:
        image_path = os.path.join(signature_img_path, img)
        content_str = InlineImage(document_template_handler, image_path, height=Mm(img_height))
        context.update({os.path.basename(image_path).split('.')[0]: content_str})
    document_template_handler.render(context)
    document_template_handler.save(save_path)


if __name__ == "__main__":
    unprocessed_path = os.path.join(os.getcwd(), 'unprocessed')
    unprocessed_docx = os.listdir(unprocessed_path)
    signature_img_path = os.path.join(os.getcwd(), 'signature_storage', 'signature')
    signature_img = os.listdir(signature_img_path)
    save_dir = os.path.join(os.getcwd(), 'document')
    for docx in unprocessed_docx:
        print("开始写入%s..." % docx)
        save_path = os.path.join(save_dir, docx)
        _, document_template_handler = create_docx_handler(os.path.join(unprocessed_path, docx), 'python-docx-template')
        signature_img_list = [s for s in signature_img if s.split('.')[0] in list(document_template_handler.get_undeclared_template_variables())]
        write(document_template_handler, signature_img_list, signature_img_path, save_path, 9)
        print("写入%s完成" % docx)
    input("任意键退出.")
