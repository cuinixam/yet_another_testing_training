project = "Yet Another Testing Training"
copyright = "2025, Alexandru Maxiniuc"
author = "Alexandru Maxiniuc"

extensions = []
extensions.append("sphinx_design")
extensions.append("myst_parser")
myst_enable_extensions = ["colon_fence", "deflist", "html_admonition", "html_image", "attrs_inline"]
# Use the mermaid extension to render diagrams.
extensions.append("sphinxcontrib.mermaid")
# To be able to copy code snippets.
extensions.append("sphinx_copybutton")


# Select only markdown files.
source_suffix = [
    ".md",
]
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "presentations"]


# Configure HTML output
html_theme = "pydata_sphinx_theme"
html_logo = "_static/logo.png"
html_title = "Yet Another Testing Training"
html_sidebars = {
    "**": ["sidebar-nav-bs"],
}
html_theme_options = {
    "icon_links": [
        {
            "name": "",
            "url": "https://www.maxiniuc.com",
            "icon": "fa-solid fa-address-card",
        }
    ],
    "secondary_sidebar_items": [],
}
html_last_updated_fmt = ""
html_static_path = ["_static"]
html_extra_path = ["presentations"]
