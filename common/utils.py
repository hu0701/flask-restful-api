from pathlib import Path


def get_attachments_path():  # 工具定义了一个函数，用于获取附件路径
    home_path = Path(__file__).parent.parent  # 使用Path类获取当前文件所在目录的父目录的路径
    attachments_path = home_path.joinpath("attachment")  # 定义附件路径为父目录下的attachment文件夹

    if not attachments_path.exists():  # 判断目录文件夹是否存在
        attachments_path.mkdir(parents=True)  # 如果不存在，则创建目录文件夹

    return attachments_path  # 返回附件路径
