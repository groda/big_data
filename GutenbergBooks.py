# This file was generated from GutenbergBooks.ipynb with nbconvert
# Source: https://github.com/groda/big_data

 #!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/groda/big_data/blob/master/GutenbergBooks.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# <a href="https://github.com/groda/big_data"><div><img src="https://github.com/groda/big_data/blob/master/logo_bdb.png?raw=true" align=right width="90" alt="Logo Big Data for Beginners"></div></a>
# # Explore and download books from the Gutenberg Books collection
# 
# This Jupyter Notebook provides an interactive exploration and downloading interface for the Gutenberg Books Collection.
# 
# Explore the vast collection of books, analyze metadata, and download selected texts based on various criteria. Dive into literary exploration and access timeless classics with ease
# 
# **Note:** you can execute the whole "Preliminaries" section while it is collapsed by clicking on the "run" icon. Once all the cells in the "Preliminaries" section have been executed, all other cells can be executed independently of one another.
# 

# ![preliminaries_collapse.png](data:image/png;base64,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)

# # Preliminaries

# ## Main class `GutenbergBooks`

# In[ ]:


import gzip
import urllib.request
import requests
import os
import io
import pandas as pd

GUTENBERG_URL = "https://www.gutenberg.org/cache/epub/feeds/pg_catalog.csv.gz"
GUTENBERG_CACHEDIR = "GutenbergBooks"

pd.options.mode.copy_on_write = True

class GutenbergBooks:
    def __init__(self):
        self.catalog_url = GUTENBERG_URL
        self.catalog_file = self.catalog_url.rsplit('/', 1)[-1][:-3]
        self.is_cached = os.path.isfile(self.catalog_file)
        self.catalog = self.fetch_catalog()
        self.all_subjects = self.get_subjects()
        self.cachedir = GUTENBERG_CACHEDIR

        if not os.path.exists(self.cachedir):
            os.makedirs(self.cachedir)

    def is_cached(self):
        if os.path.isfile(self.catalog_file):
            return True
        return False

    def cache_catalog(self):
        self.catalog = self.fetch_catalog(use_cache=False)
        self.catalog.to_csv(self.catalog_file)
        self.is_cached = True

    def is_book_downloaded(self, bookID):
        book_file = f"pg{bookID}.txt"
        if os.path.isfile(os.path.join(GUTENBERG_CACHEDIR, book_file)):
          return True
        return False

    def fetch_catalog(self, use_cache=True):
        url = self.catalog_url
        filename = self.catalog_file
        if self.is_cached and use_cache:
            print(f"Retrieving {filename} from cache. To refresh cache use cache_catalog()")
            dataframe = pd.read_csv(filename, quotechar = '"')
            return dataframe
        try:
            # Retrieve the compressed file from the URL
            print(f"Retrieving {filename} from {url}.")
            response = urllib.request.urlopen(url)
            compressed_data = response.read()
            # Decompress the data
            decompressed_data = gzip.decompress(compressed_data)
            # Load decompressed data into pandas DataFrame
            dataframe = pd.read_csv(io.StringIO(decompressed_data.decode('utf-8')), quotechar = '"')
            dataframe.to_csv(self.catalog_file)
            self.is_cached = True
            return dataframe
        except Exception as e:
            print("An error occurred:", e)
            return None

    def get_subjects(self):
        return self.catalog['Subjects'].str.split('; ').explode().unique().tolist()

    def random_subjects(self, n, seed):
        """
        This method returns n random subjects.
        Parameters:
        - n (int): number of subjects.
        - seed (int): random seed for reproducibility.
        Returns:
        - list: Random sample of subjects from the Gutenberg Books catalog
                following the subjects distribution.
        """
        df = self.catalog['Subjects']
        subject_counts = df.str.split('; ').explode() \
                           .groupby(df.str.split('; ').explode()).count() \
                           .reset_index(name='Count').sort_values(by='Count', ascending=False) \
                           .rename(columns={"Subjects": "Subject"}) \
                           .reset_index(drop=True)
        return subject_counts.sample(n=n, replace=False, random_state=seed, weights=subject_counts['Count'])

    def topn_subjects(self, n):
        df = self.catalog['Subjects']
        subject_counts = df.str.split('; ').explode() \
                           .groupby(df.str.split('; ').explode()).count() \
                           .reset_index(name='Count').sort_values(by='Count', ascending=False) \
                           .rename(columns={"Subjects": "Subject"})
        return subject_counts.reset_index(drop=True).head(n)

    def get_authors(self):
        return self.catalog['Authors'].str.split('; ').explode().unique().tolist()

    def random_authors(self, n, seed):
        df = self.catalog['Authors']
        author_counts = df.str.split('; ').explode() \
                           .groupby(df.str.split('; ').explode()).count() \
                           .reset_index(name='Count').sort_values(by='Count', ascending=False) \
                           .rename(columns={"Authors": "Author"}) \
                           .reset_index(drop=True)
        return author_counts.sample(n=n, replace=False, random_state=seed, weights=author_counts['Count'])

    def topn_authors(self, n):
        df = self.catalog['Authors']
        author_counts = df.str.split('; ').explode() \
                           .groupby(df.str.split('; ').explode()).count() \
                           .reset_index(name='Count').sort_values(by='Count', ascending=False) \
                           .rename(columns={"Authors": "Author"})
        return author_counts.reset_index(drop=True).head(n)

    def get_languages(self):
        return self.catalog['Language'].str.split('; ').explode().unique().tolist()

    def topn_languages(self, n):
        df = self.catalog['Language']
        language_counts = df.str.split('; ').explode() \
                            .groupby(df.str.split('; ').explode()).count() \
                            .reset_index(name='Count').sort_values(by='Count', ascending=False)
        return language_counts.reset_index(drop=True).head(n)

    def get_bookshelves(self):
        return self.catalog['Bookshelves'].str.split('; ').explode().unique().tolist()

    def topn_bookshelves(self, n):
        df = self.catalog['Bookshelves']
        bookshelf_counts = df.str.split('; ').explode() \
                             .groupby(df.str.split('; ').explode()).count() \
                             .reset_index(name='Count').sort_values(by='Count', ascending=False) \
                             .rename(columns={"Bookshelves": "Bookshelf"})
        return bookshelf_counts.reset_index(drop=True).head(n)

    def get_types(self):
        return self.catalog['Type'].unique().tolist()

    def get_books(self, lang, subject, title):
        return self.catalog.sample(n=n, replace=False, random_state=seed)

    def random_books(self, n, seed):
        return self.catalog.sample(n=n, replace=False, random_state=seed)

    def books_matching_subject(self, substr):
        return self.catalog.query(f'Subjects.str.lower().str.contains("{substr.lower()}", na=False)')

    def books_matching_author(self, substr):
        return self.catalog.query(f'Author.str.lower().str.contains("{substr.lower()}", na=False)')

    def books_matching_year(self, given_year):
        """
        Find books from the catalog that match a given year within the birth-death intervals of authors.

        Parameters:
        - given_year (int): The year to match within the birth-death intervals of authors.

        Returns:
        - DataFrame: A DataFrame containing books from the catalog where the given year falls within
                     the birth-death intervals of authors.

        This method extracts birth and death years from the 'Authors' column of the catalog and filters
        rows where the given year is within any birth-death interval. It returns a DataFrame of matching books.
        """
        catalog_copy = self.catalog.copy()
        # Create a temporary DataFrame to hold split author-interval pairs
        temp_df = catalog_copy['Authors'].str.extractall(r'((?:\w+\s+)?(?:\d{4})\s*-\s*(?:\d{4}))')
        temp_df.reset_index(inplace=True)
        temp_df.rename(columns={0: 'Author_Interval'}, inplace=True)
        # Merge the original catalog with the temporary DataFrame
        merged_df = pd.merge(catalog_copy, temp_df, left_index=True, right_on='level_0')
        # Extract birth and death years from the author-interval pairs
        merged_df['Birth_Year'] = merged_df['Author_Interval'].str.extract(r'(\d{4})')
        merged_df['Death_Year'] = merged_df['Author_Interval'].str.extract(r'\d{4}\s*-\s*(\d{4})')
        # Convert birth and death years to numeric
        merged_df['Birth_Year'] = pd.to_numeric(merged_df['Birth_Year'], errors='coerce')
        merged_df['Death_Year'] = pd.to_numeric(merged_df['Death_Year'], errors='coerce')
        # Filter rows where the given year is within any birth-death interval
        matching_books = merged_df[(merged_df['Birth_Year'] <= given_year) &
                               (merged_df['Death_Year'] >= given_year)]
        # Drop unnecessary columns
        matching_books.drop(columns=['Author_Interval', 'level_0'], inplace=True)
        # Return matching books
        return matching_books

    def download_book(self, nr):
        """
        Download one book from the Gutenberg collection identified by its id.
        If the book already exists in the cache folder, it is not downloaded again.
        Parameters:
        - nr (int): id of the book in the Gutenberg books collection.
        Returns:
        - str: the path where the book was downloaded.
        """
        b = str(nr)
        book = f"pg{b}.txt"
        url = f"https://www.gutenberg.org/cache/epub/{b}/{book}"
        book_path = os.path.join(GUTENBERG_CACHEDIR, book)
        if self.is_book_downloaded(b):
            print(f"Book {nr} already exists in cache. Not downloading.")
        else:
            try:
            # Retrieve the book from the URL
                print(f"Retrieving {book} from {url}.")
                with open(book_path, "w") as f:
                    f.write(requests.get(url).text)
            except Exception as e:
                print("An error occurred:", e)
                return None
        return book_path

    def download_books(self, books):
        """
        Download a list of books from the Gutenberg collection.
        If a book already exists in the cache folder, it is not downloaded again.
        Parameters:
        - books (list): list of ids of books in the Gutenberg books collection.
        Returns:
        - str: the path where the book was downloaded.
        """
        book_paths = []
        for b in books:
          path =self.download_book(b)
          book_paths += [path]
        return book_paths

    def download_n_books(self, n, subject):
        """
        Download a certain number of books from the Gutenberg collection based on the desired size and subject.
        If a book already exists in the cache folder, it is not downloaded again.

        Parameters:
        - n (int): The number of books to download.
        - subject (str): The subject to match when selecting books.

        Returns:
        - list: A list of paths where the downloaded books are saved.
        """
        # Get books matching the subject
        matching_books = self.books_matching_subject(subject)
        # Limit the number of books to download
        books_to_download = matching_books[:n]['Text#']
        # Download books
        book_paths = [self.download_book(b) for b in books_to_download]
        return book_paths

    def download_size_books(self, size_mb=128, subject=None):
        """
        Download books from the Gutenberg collection based on the desired total size and subject.
        If a book already exists in the cache folder, it is not downloaded again.

        Parameters:
        - size_mb (int): The desired total size of downloaded books in MB. Default is 128MB.
        - subject (str, optional): The subject to match when selecting books. Default is None.

        Returns:
        - list: A list of paths where the downloaded books are saved.
        """
        # Get books matching the subject if provided
        if subject:
            matching_books = self.books_matching_subject(subject)['Text#']
        else:
            matching_books = self.catalog['Text#']
        # Initialize variables
        total_size = 0
        books_to_download = []
        # Iterate through matching books until total size threshold is met
        for b in matching_books:
            if total_size >= size_mb * 1024 * 1024:  # Convert MB to bytes
                break
            book_path = self.download_book(b)
            file_size = os.path.getsize(book_path)
            # Add file size to total size
            total_size += file_size
            # Add book to download list
            books_to_download.append(b)
        # Download books
        book_paths = [self.download_book(b) for b in books_to_download]
        print(f"Total size: {int(total_size/1024/1024)}MB")
        if total_size <= size_mb * 1024 * 1024:
          print(f"Download more books to get {size_mb}MB")
        return book_paths

gb = GutenbergBooks()


# ## Use `cache_catalog()` to create a cached copy of the catalog

# In[ ]:


# gb.cache_catalog()


# ## Interactive tables
# 
# Library `data_table` from Google Colab adds interactivity to Pandas tables.
# 
# https://colab.research.google.com/notebooks/data_table.ipynb

# In[ ]:


# true if running on Google Colab
import sys
IN_COLAB = 'google.colab' in sys.modules

if IN_COLAB:
  from google.colab import data_table
  from vega_datasets import data
  data_table.enable_dataframe_formatter()
else:
  get_ipython().system('pip install itables')
  from itables import init_notebook_mode
  init_notebook_mode(all_interactive=True)


# ## Code for visualizations
# 
# This is needed for plotting.

# In[ ]:


import matplotlib
colors = matplotlib.cm.tab20(range(20))

# source: https://matplotlib.org/stable/gallery/misc/packed_bubbles.html
import matplotlib.pyplot as plt
import numpy as np

class BubbleChart:
    def __init__(self, area, bubble_spacing=0):
        """
        Setup for bubble collapse.

        Parameters
        ----------
        area : array-like
            Area of the bubbles.
        bubble_spacing : float, default: 0
            Minimal spacing between bubbles after collapsing.

        Notes
        -----
        If "area" is sorted, the results might look weird.
        """
        area = np.asarray(area)
        r = np.sqrt(area / np.pi)

        self.bubble_spacing = bubble_spacing
        self.bubbles = np.ones((len(area), 4))
        self.bubbles[:, 2] = r
        self.bubbles[:, 3] = area
        self.maxstep = 2 * self.bubbles[:, 2].max() + self.bubble_spacing
        self.step_dist = self.maxstep / 2

        # calculate initial grid layout for bubbles
        length = np.ceil(np.sqrt(len(self.bubbles)))
        grid = np.arange(length) * self.maxstep
        gx, gy = np.meshgrid(grid, grid)
        self.bubbles[:, 0] = gx.flatten()[:len(self.bubbles)]
        self.bubbles[:, 1] = gy.flatten()[:len(self.bubbles)]

        self.com = self.center_of_mass()

    def center_of_mass(self):
        return np.average(
            self.bubbles[:, :2], axis=0, weights=self.bubbles[:, 3]
        )

    def center_distance(self, bubble, bubbles):
        return np.hypot(bubble[0] - bubbles[:, 0],
                        bubble[1] - bubbles[:, 1])

    def outline_distance(self, bubble, bubbles):
        center_distance = self.center_distance(bubble, bubbles)
        return center_distance - bubble[2] - \
            bubbles[:, 2] - self.bubble_spacing

    def check_collisions(self, bubble, bubbles):
        distance = self.outline_distance(bubble, bubbles)
        return len(distance[distance < 0])

    def collides_with(self, bubble, bubbles):
        distance = self.outline_distance(bubble, bubbles)
        return np.argmin(distance, keepdims=True)

    def collapse(self, n_iterations=50):
        """
        Move bubbles to the center of mass.

        Parameters
        ----------
        n_iterations : int, default: 100
            Number of moves to perform.
        """
        for _i in range(n_iterations):
            moves = 0
            for i in range(len(self.bubbles)):
                rest_bub = np.delete(self.bubbles, i, 0)
                # try to move directly towards the center of mass
                # direction vector from bubble to the center of mass
                dir_vec = self.com - self.bubbles[i, :2]

                # shorten direction vector to have length of 1
                dir_vec = dir_vec / np.sqrt(dir_vec.dot(dir_vec))

                # calculate new bubble position
                new_point = self.bubbles[i, :2] + dir_vec * self.step_dist
                new_bubble = np.append(new_point, self.bubbles[i, 2:4])

                # check whether new bubble collides with other bubbles
                if not self.check_collisions(new_bubble, rest_bub):
                    self.bubbles[i, :] = new_bubble
                    self.com = self.center_of_mass()
                    moves += 1
                else:
                    # try to move around a bubble that you collide with
                    # find colliding bubble
                    for colliding in self.collides_with(new_bubble, rest_bub):
                        # calculate direction vector
                        dir_vec = rest_bub[colliding, :2] - self.bubbles[i, :2]
                        dir_vec = dir_vec / np.sqrt(dir_vec.dot(dir_vec))
                        # calculate orthogonal vector
                        orth = np.array([dir_vec[1], -dir_vec[0]])
                        # test which direction to go
                        new_point1 = (self.bubbles[i, :2] + orth *
                                      self.step_dist)
                        new_point2 = (self.bubbles[i, :2] - orth *
                                      self.step_dist)
                        dist1 = self.center_distance(
                            self.com, np.array([new_point1]))
                        dist2 = self.center_distance(
                            self.com, np.array([new_point2]))
                        new_point = new_point1 if dist1 < dist2 else new_point2
                        new_bubble = np.append(new_point, self.bubbles[i, 2:4])
                        if not self.check_collisions(new_bubble, rest_bub):
                            self.bubbles[i, :] = new_bubble
                            self.com = self.center_of_mass()

            if moves / len(self.bubbles) < 0.1:
                self.step_dist = self.step_dist / 2

    def plot(self, ax, labels, colors):
        """
        Draw the bubble plot.

        Parameters
        ----------
        ax : matplotlib.axes.Axes
        labels : list
            Labels of the bubbles.
        colors : list
            Colors of the bubbles.
        """
        for i in range(len(self.bubbles)):
            circ = plt.Circle(
                self.bubbles[i, :2], self.bubbles[i, 2], color=colors[i])
            ax.add_patch(circ)
            ax.text(*self.bubbles[i, :2], labels[i],
                    horizontalalignment='center', verticalalignment='center')

# Attempt to set the font family
desired_font_family = 'DejaVu Serif'
try:
    plt.rcParams['font.family'] = desired_font_family
    print(f"Using '{desired_font_family}' font family.")
except:
    print(f"Warning: Font family '{desired_font_family}' not found. Using fallback font.")
    plt.rcParams['font.family'] = 'serif'  # Fallback to a generic serif font


# # Explore

# ## Books

# ### All books
# 
# The whole Gutenberg collection catalog is saved in the `catalog` of the `GutenbergBooks` object `gb`.

# In[ ]:


gb.catalog


# ### Count books in the collection
# 
# There are currently $73109$ books in the collection.

# In[ ]:


len(gb.catalog)


# ### First five books in the catalog

# In[ ]:


gb.catalog.head(5)


# ### Five random books
# 
# Looking only at the first lines of a DataFrame might provide an initial glimpse into the data, but it can be insufficient for gaining a comprehensive understanding of its characteristics, that's why sampling from the DataFrame is often more beneficial.
# 
# So, let's break away from the norm of quickly scanning the first few lines of a file with the `head` command. Let us instead allocate a bit more computational power and extract a small yet representative sample of the data.

# In[ ]:


print("Five random books from catalog")
gb.random_books(n=5, seed=42)


# ## Subjects

# ### Count distinct subjects
# 
# There are currently $39619$ distinct subjects.

# In[ ]:


len(gb.get_subjects())


# ### Top $n$ subjects

# In[ ]:


n = 10
gb.topn_subjects(n)


# ### 20K subjects

# In[ ]:


pd.DataFrame(gb.topn_subjects(20000))
# Limiting the number of rows to 20000 because this is the maximum number supported
# by Colab's `data_table`.


# ### Ten random subjects

# In[ ]:


gb.random_subjects(10, 42).sort_values(by='Count', ascending=False)


# ### List books matching a given subject
# 
# Change the subject by setting the variable `my_subject` (search is case-insensitive).

# In[ ]:


substr = "description and travel"
gb.books_matching_subject(substr).head()


# ### Visualize most frequent subjects

# In[ ]:


n = 20
gutenberg_books_subjects = {
    'subjects': gb.topn_subjects(n)['Subject'].replace({' -- ': '
'}, regex=True).to_list(),
    'market_share': list(map(lambda x: x*n*3, gb.topn_subjects(n)['Count'].to_list())),
    'color': colors[:n]
}

bubble_chart = BubbleChart(area=gutenberg_books_subjects['market_share'],
                           bubble_spacing=2*n)

bubble_chart.collapse()

fig, ax = plt.subplots(subplot_kw=dict(aspect="equal"), figsize=(10, 10))
bubble_chart.plot(
    ax, gutenberg_books_subjects['subjects'], gutenberg_books_subjects['color'])
ax.axis("off")
ax.relim()
ax.autoscale_view()
ax.set_title(f'Gutenberg books top {n} subjects')

plt.show()


# ## Authors

# ### Count distinct authors
# 
# There are currently $37392$ distinct authors.

# In[ ]:


len(gb.get_authors())


# ### All authors
# The `data_table` library can only deal with a maximum of $20000$ rows. If the number of rows exceeds this limit, the usual Pandas display is used (with no interactivity).
# 

# In[ ]:


pd.DataFrame(gb.get_authors())


# ### Top $n$ authors

# In[ ]:


n = 20000
gb.topn_authors(n)


# ### Ten random authors

# In[ ]:


gb.random_authors(10, 42).sort_values(by='Count', ascending=False)


# ### Visualize most frequent authors

# In[ ]:


n = 20
gutenberg_books_authors = {
    'authors': gb.topn_authors(n)['Author'].replace({', ': '
', ' \[': '
['}, regex=True).to_list(),
    'market_share': list(map(lambda x: x*n*3, gb.topn_authors(n)['Count'].to_list())),
    'color': colors[:n]
}

bubble_chart = BubbleChart(area=gutenberg_books_authors['market_share'],
                           bubble_spacing=2*n)

bubble_chart.collapse()

fig, ax = plt.subplots(subplot_kw=dict(aspect="equal"),figsize=(10, 10))
bubble_chart.plot(
    ax, gutenberg_books_authors['authors'], gutenberg_books_authors['color'])
ax.axis("off")
ax.relim()
ax.autoscale_view()
ax.set_title(f'Gutenberg books top {n} authors')

plt.show()


# ## Types

# ### All types

# In[ ]:


pd.DataFrame(gb.get_types(), columns=['Type'])


# ### Count books by types

# In[ ]:


grouped_counts = gb.catalog.groupby('Type').size().reset_index(name='Count')
grouped_counts


# ### Visualize types

# In[ ]:


grouped_data = gb.catalog.groupby('Type').size().reset_index(name='Count')
n = len(grouped_data)
# Extracting values of 'Type' and 'Count' columns as lists
type_list = grouped_data['Type'].tolist()
count_list = grouped_data['Count'].tolist()
gutenberg_books_types = {
    'types': type_list,
    # adapt the size of smaller items
    'market_share': list(map(lambda x: x if x>1000 else x*n*10, count_list)),
    'color': colors[:-n]
}

bubble_chart = BubbleChart(area=gutenberg_books_types['market_share'],
                           bubble_spacing=2*n)

bubble_chart.collapse()

fig, ax = plt.subplots(subplot_kw=dict(aspect="equal"),figsize=(10, 10))
bubble_chart.plot(
    ax, gutenberg_books_types['types'], gutenberg_books_types['color'])
ax.axis("off")
ax.relim()
ax.autoscale_view()
ax.set_title(f'Gutenberg books top types')
subtitle = "(the depicted proportions have been altered and do not reflect the true distribution)"
# Set the subtitle below the main title
plt.text(0.5, 0.98, subtitle, fontsize=10, ha='center', transform=plt.gca().transAxes)

plt.show()


# I wasn't aware that the Gutenberg collection contained data other than text. I'll need to explore these additional data types at some point.

# ## Bookshelves

# ### Top $n$ bookshelves

# In[ ]:


n = 10
gb.topn_bookshelves(n)


# ### Visualize most frequent bookshelves

# In[ ]:


n = 20
gutenberg_books_bookshelves = {
    'bookshelves': gb.topn_bookshelves(n)['Bookshelf'].replace({', ': '
'}, regex=True).to_list(),
    'market_share': list(map(lambda x: x*n*3, gb.topn_bookshelves(n)['Count'].to_list())),
    'color': colors[:n]
}

bubble_chart = BubbleChart(area=gutenberg_books_bookshelves['market_share'],
                           bubble_spacing=4*n)

bubble_chart.collapse()

fig, ax = plt.subplots(subplot_kw=dict(aspect="equal"), figsize=(10, 10))
bubble_chart.plot(
    ax, gutenberg_books_bookshelves['bookshelves'], gutenberg_books_bookshelves['color'])
ax.axis("off")
ax.relim()
ax.autoscale_view()
ax.set_title(f'Gutenberg books top {n} bookshelves')

plt.show()


# ### Books without bookshelf
# 
# Many books do not belong to any bookshelf

# In[ ]:


gb.catalog.count()


# ### Number of books without bookshelf

# In[ ]:


print(f"Number of books with no bookshelf: {gb.catalog[gb.catalog['Bookshelves'].isna()].shape[0]}")


# ### Five random books without bookshelf

# In[ ]:


gb.catalog[gb.catalog['Bookshelves'].isna()].sample(n=5, replace=False, random_state=42)


# ## Languages

# ### Count distinct languages
# 
# The Gutenberg collection currently comprises 68 languages.

# In[ ]:


len(gb.get_languages())


# ### Top $n$ languages

# In[ ]:


gb.topn_languages(10)


# ### Visualize top $n$ languages

# In[ ]:


n = 20
gutenberg_books_languages = {
    'languages': gb.topn_languages(n)['Language'].to_list(),
    'market_share': list(map(lambda x: x*10, gb.topn_languages(n)['Count'].to_list())),
    'color': colors
}

bubble_chart = BubbleChart(area=gutenberg_books_languages['market_share'],
                           bubble_spacing=15)

bubble_chart.collapse()

fig, ax = plt.subplots(subplot_kw=dict(aspect="equal"), figsize=(10, 10))
bubble_chart.plot(
    ax, gutenberg_books_languages['languages'], gutenberg_books_languages['color'])
ax.axis("off")
ax.relim()
ax.autoscale_view()
ax.set_title(f'Gutenberg books top {n} languages')

plt.show()


# ## Match books using various criteria

# ### Match books by subject

# In[ ]:


substr = "description and travel"
gb.books_matching_subject(substr)


# ### Match books by year

# In[ ]:


gb.books_matching_year(1984)


# In[ ]:


help(GutenbergBooks.books_matching_year)


# # Downloading files from the Gutenberg collection
# 
# ⚠️ Please read carefully this notice about the Gutenberg Project's policies on bulk downloading:
# 
# 
# 
# > “ _The Project Gutenberg website is intended for human users only. Any perceived use of automated tools to access the Project Gutenberg website will result in a temporary or permanent block of your IP address._ ”
# 
# See: https://www.gutenberg.org/policy/robot_access.html.
# 

# ## The cache directory
# 
# By default, `GutenbergBooks` is the directory where all downloaded books are stored. If a book is alredy in the `GutenbergBooks` directory it won't be downloaded again.
# 
# ⚠️ The cache directory is empty when you start your Google Colab session! ⚠️

# ## Download one book

# In[ ]:


gb.download_book(5687)


# The same book won't be downloaded because it already exists in the cache directory `GutenbergBooks`.

# In[ ]:


gb.download_book(5687)


# In[ ]:


help(GutenbergBooks.download_book)


# ## Download multiple books

# In[ ]:


gb.download_books([5678, 5679, 5680])


# In[ ]:


help(GutenbergBooks.download_books)


# ## Download $n$ books by subject

# In[ ]:


gb.download_n_books(5, "\(South Africa\) -- Description and travel")


# ## Download a given amount of books by subject
# 
# DOwnload books matching a certain subject. Stop when the threshold given by the `size_mb` (size in Megabytes) parameter is reached.
# 
# If not specified, `size_mb` is $128$ (the default Hadoop block size).

# In[ ]:


gb.download_size_books(subject="\(South Africa\) -- Description and travel")


# In[ ]:


get_ipython().system('du -sh GutenbergBooks')


# In[ ]:


subject = "United States -- Description and travel"
gb.download_size_books(size_mb=90, subject=subject)


# In[ ]:


get_ipython().system('du -sh GutenbergBooks')


# It's not easy to get enough data!

# In[ ]:


subject = "California -- Description and travel"
gb.download_size_books(size_mb=50, subject=subject)


# In[ ]:


get_ipython().system('du -sh GutenbergBooks')


# # Acknowledgements and some thoughts on Artificial Intelligence
# 
# For this tutorial I've made extensive use of the ChatGPT (version $3.5$) AI to:
# - improve my English
# - define code structure
# - write Python code snippets
# - document code
# 
# I ideated, organized, adapted, double-checked all content (both text and code) with the aim of creating a useful tool for exploring the Gutenberg books collection and providing a pleasant user experience.
# 
# I can imagine that in the future AI will be able to write such tutorials on their own and then the role of a tutorial author will be limited to defining requirements. Maybe there are going to be self-adapting tutorials that create themselves on the spot according to the needs of the readers, thus bypassing the need for tutorial authors. What are tutorial authors going to do then? Something else 😀!
# 
# 
# In this spirit, I'd like to thank everyone who contributed to the common sense language collection (both natural and programming languages) used to train ChatGPT, the creators of ChatGPT, and the companies making it available as a comfortable Web application.
