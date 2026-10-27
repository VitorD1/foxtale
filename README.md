# FoxTale

FoxTale is a small website for a fictional art atelier that makes hand-decorated gifts: bottles, boxes, panels, candle holders and napkin holders.
Visitors can browse the products, filter and sort them, and read stories and gift ideas.
The owner adds, edits and deletes products and articles directly from the site.

## Features

- Product gallery with filter by category and occasion, and sorting by newest, price or name
- Product details, create, edit and delete with confirmation
- Articles in four sections: About, Mission, History and Ideas
- Article details with reading time and recommended products, create, edit and delete with confirmation
- Categories and occasions with product counters
- Home page with carousels for the newest products and articles
- Custom 404 page

## Tech Stack

- Python 3.13
- Django 6.1
- Pillow (image uploads)
- SQLite
- Bootstrap 5.3 (CDN)

## Installation

Download or clone the repository and open the project folder.

Create a virtual environment:

    python -m venv .venv

Activate it on Windows:

    .venv\Scripts\activate

Activate it on macOS / Linux:

    source .venv/bin/activate

Install the dependencies:

    pip install -r requirements.txt

Create the database:

    python manage.py migrate

## Usage

Start the development server:

    python manage.py runserver

Open http://127.0.0.1:8000/ in the browser.

The database starts empty. No admin account is needed, everything is created through the site:

1. **Categories** → add a category
2. **Occasions** → add an occasion
3. **Products** → add a product (with a photo up to 5 MB)
4. **Articles** → add an article

## Project Structure

    foxtale/
    ├── foxtale/       settings and main urls
    ├── common/        home page, custom template tags
    ├── products/      Category, Occasion, Product
    ├── stories/       Article
    ├── templates/     base, partials, pages for each app, 404
    ├── static/        css and logo
    ├── manage.py
    └── requirements.txt

## Database

| Model | Relations |
|---|---|
| Category | one category has many products |
| Occasion | many-to-many with Product, one occasion has many articles |
| Product | ForeignKey to Category (PROTECT), many-to-many with Occasion |
| Article | ForeignKey to Occasion (SET_NULL), many-to-many with Product |

Extra model details:

- unique product title inside a category (`UniqueConstraint`)
- category name only with letters and spaces (`RegexValidator`)
- custom image size validator (up to 5 MB)
- `TextChoices` for the article sections
- default ordering in `Meta`

## Forms and Validation

- `CategoryForm`, `OccasionForm`, `ProductForm`, `ArticleForm` with labels, placeholders, help texts and custom error messages
- `ProductEditForm` and `ArticleEditForm`: the category and the section are read-only when editing
- `ArticleForm.clean()`: an occasion can be chosen only for the Ideas section, and there can be only one About article
- `ProductFilterForm`: GET form for filtering and sorting
- `created_at` is excluded from the forms

## Views

- Class-based views: `ListView`, `DetailView`, `CreateView`, `UpdateView`, `DeleteView`, `TemplateView`
- `get_queryset()` for filtering, sorting and sections, `get_context_data()` for extra data
- `Http404` for an unknown section

## Templates

- `base.html` with navigation and footer as partials
- reusable partials for forms and article cards
- built-in filters: `date`, `truncatewords`, `linebreaks`, `floatformat`
- custom template tags in `common/templatetags/fox_tags.py`:
  - `reading_time` filter: minutes needed to read an article
  - `products_count` tag: total number of products in the footer

## Author

VitorD1, SoftUni Python Web Basics, test exam project, 2026