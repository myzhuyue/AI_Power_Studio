import random
import re
import os
from datetime import datetime

def read_file(file_path):
    """
    读取指定路径的文件内容
    :param file_path: 文件路径
    :return: 文件内容
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"未找到文件: {file_path}")
        return None
    except Exception as e:
        print(f"读取文件时出现错误: {e}")
        return None

def extract_question_links(content):
    """
    从文件内容中提取 Part 4 - Programming & Visualization 部分的题目链接
    :param content: 文件内容
    :return: 题目链接列表
    """
    start_index = content.find('## Part 4 - Programming & Visualization')
    if start_index == -1:
        print("未找到 'Part 4 - Programming & Visualization' 部分。")
        return []
    part_4_content = content[start_index:]
    question_links = re.findall(r'\[(.*?)\]\((.*?)\)', part_4_content)
    return [link[1] for link in question_links]

def select_question_links(question_links):
    """
    从题目链接列表中随机抽取 10 个链接
    :param question_links: 题目链接列表
    :return: 抽取的题目链接列表
    """
    if len(question_links) >= 10:
        return random.sample(question_links, 10)
    else:
        print("该部分的题目数量少于 10 道，无法抽取 10 道题。将使用所有题目。")
        return question_links

def read_question_content(question_link):
    """
    读取指定题目链接对应的 Markdown 文件内容
    :param question_link: 题目链接
    :return: 题目 Markdown 文件内容
    """
    question_path = os.path.join('engineering-interview', question_link)
    try:
        with open(question_path, 'r', encoding='utf-8') as question_file:
            return question_file.read()
    except FileNotFoundError:
        print(f"文件 {question_path} 未找到。")
        return None
    except Exception as e:
        print(f"读取题目文件 {question_path} 时出现错误: {e}")
        return None

def clean_markdown_content(content):
    """
    清理 Markdown 内容，去除无法识别的格式
    :param content: Markdown 内容
    :return: 清理后的 Markdown 内容
    """
    # 去除 HTML 标签
    content = re.sub(r'<[^>]*>', '', content)
    # 去除连续的空行
    content = re.sub(r'\n\s*\n', '\n\n', content).strip()
    return content

def generate_markdown_content(selected_question_links):
    """
    根据抽取的题目链接生成 Markdown 内容
    :param selected_question_links: 抽取的题目链接列表
    :return: Markdown 内容
    """
    markdown_content = "# 抽取的题目\n\n"
    for question_link in selected_question_links:
        question_content = read_question_content(question_link)
        if question_content:
            cleaned_content = clean_markdown_content(question_content)
            markdown_content += f"### 题目文件: {question_link}\n\n{cleaned_content}\n\n"
    return markdown_content

def save_markdown_file(markdown_content):
    """
    将 Markdown 内容保存到以时间戳加上“笔试题目”命名的文件中
    :param markdown_content: Markdown 内容
    """
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    output_file_name = f"{timestamp}笔试题目.md"
    output_path = os.path.join('engineering-interview', output_file_name)
    try:
        with open(output_path, 'w', encoding='utf-8') as output_file:
            output_file.write(markdown_content)
        print(f"题目内容已成功保存到 {output_path} 文件中。")
    except Exception as e:
        print(f"保存文件时出现错误: {e}")

def main():
    readme_path = 'engineering-interview/readme.md'
    content = read_file(readme_path)
    if content is None:
        return
    question_links = extract_question_links(content)
    selected_question_links = select_question_links(question_links)
    markdown_content = generate_markdown_content(selected_question_links)
    save_markdown_file(markdown_content)

if __name__ == "__main__":
    main()