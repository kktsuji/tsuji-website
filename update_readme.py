"""Update README.md with the latest content"""

from datetime import date
import glob
import os


_WEBSITE_URL = "https://tsuji.tech/"
_BLOG_POSTS = "./content/blog/*/*.en.md"
_TIL_POSTS = "./content/til/*"


def _make_intro_section():
    section = "# tsuji.tech\n\n"
    section += "This is a repository of my personal website [tsuji.tech](https://tsuji.tech).\n\n"
    section += (
        "## About Me\n\n"
        "I’m Tsuji, a software engineer "
        "specialized in signal processing and camera imaging technology about CMOS image sensors. "
        "I’ve been working in semiconductor manufacturing field "
        "to develop image sensor-related technology from 2018 to the present. "
        "For more details, see [about](https://tsuji.tech/about/).\n\n"
    )
    return section


def _make_fixed_section():
    section = "## Fixed Pages\n\n"
    section += (
        "- [About](https://tsuji.tech/about/)\n"
        "- [Contact](https://tsuji.tech/contact/)\n"
        "- [Disclaimer](https://tsuji.tech/disclaimer/)\n"
        "- [Privacy Policy](https://tsuji.tech/privacy-policy/)\n"
        "- [Sitemap](https://tsuji.tech/sitemap/)\n\n"
    )
    return section


def _get_post_date_from_markdown_file(file_path):
    with open(file_path, mode="r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith("date:"):
                return date.fromisoformat(line.split(":")[1].split("T")[0].strip())
    return None


def _get_post_title_from_markdown_file(file_path):
    with open(file_path, mode="r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith("title:"):
                return line[7:]
    return None


def _make_blog_posts_section():
    date_post_pairs = [
        [_get_post_date_from_markdown_file(post), post]
        for post in glob.glob(_BLOG_POSTS)
    ]
    date_post_pairs.sort(key=lambda x: x[0], reverse=True)

    section = "## Blog Posts\n\n"
    section += (
        f"There are {len(date_post_pairs)} [blog](https://tsuji.tech/blog/) posts.\n\n"
    )
    for post_date, post in date_post_pairs:
        post_url = post.split("/")[-1].replace(".en.md", "")
        url_en = _WEBSITE_URL + post_url
        url_jp = _WEBSITE_URL + "/jp/" + post_url
        title = _get_post_title_from_markdown_file(post)
        section += (
            f"- [{title[1:-2]}]({url_en}) ([JP]({url_jp})) "
            f"({post_date.strftime("%b %-d, %Y")})\n"
        )
    section += "\n"

    return section


def _make_til_posts_section():
    til_categories = [item for item in glob.glob(_TIL_POSTS) if os.path.isdir(item)]
    til_categories.sort()
    post_num = len(
        [post for post in glob.glob(_TIL_POSTS + "/*.md") if not "_index" in post]
    )

    section = "## TIL (Today I Learned) Posts\n\n"
    section += f"There are {post_num} [TIL](https://tsuji.tech/til/) posts.\n\n"
    for category in til_categories:
        category_name = category.split("/")[-1]
        section += f"### {category_name}\n\n"

        posts = [post for post in glob.glob(category + "/*.md") if not "_index" in post]
        date_post_pairs = [
            [_get_post_date_from_markdown_file(post), post] for post in posts
        ]
        date_post_pairs.sort(key=lambda x: x[0], reverse=True)

        for post_date, post in date_post_pairs:
            url = _WEBSITE_URL + post.split("/")[-1].replace(".md", "")
            title = _get_post_title_from_markdown_file(post)
            section += (
                f"- [{title[1:-2]}]({url}) ({post_date.strftime("%b %-d, %Y")})\n"
            )
        section += "\n"

    return section


def update_readme():
    """Update README.md with the latest content"""
    intro_section = _make_intro_section()
    fixed_section = _make_fixed_section()
    blog_posts_section = _make_blog_posts_section()
    til_posts_section = _make_til_posts_section()

    with open("README.md", mode="w", encoding="utf-8") as f:
        f.write(intro_section)
        f.write(fixed_section)
        f.write(blog_posts_section)
        f.write(til_posts_section[:-1])


if __name__ == "__main__":
    update_readme()
