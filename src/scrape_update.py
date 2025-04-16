import asyncio

from modules.scrape_update_module import scrape_update


def main():
    path = input("请输入本地帖子数据的路径: ")
    asyncio.run(scrape_update(path))


if __name__ == "__main__":
    main()
