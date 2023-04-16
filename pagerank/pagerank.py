import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    N = len(corpus)
    model = {}

    for pg in corpus:
        page_rank = (1 - damping_factor) / N
        if len(corpus[page]):
            if pg in corpus[page]:
                page_rank += damping_factor / len(corpus[page])
        else:
            page_rank += damping_factor / N
        model[pg] = page_rank
    return model


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    page_ranks = {page: 0 for page in corpus}
    current_page = random.choice(list(corpus.keys()))

    for _ in range(n):
        page_ranks[current_page] += 1
        model = transition_model(corpus, current_page, damping_factor)
        current_page = random.choice(list(model.keys()))
    return {page: rank / n for page, rank in page_ranks.items()}


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    N = len(corpus)
    previous_ranks = {}

    for page in corpus:
        previous_ranks[page] = 1 / N
    while True:
        current_ranks = {}
        for current_page in corpus:
            current_page_rank = (1 - damping_factor) / N
            for page, links in corpus.items():
                if links:
                    if page != current_page and current_page in links:
                        current_page_rank += damping_factor * (previous_ranks[page] / len(corpus[page]))
                else:
                    current_page_rank += damping_factor * (previous_ranks[page] / N)
            current_ranks[current_page] = current_page_rank

        # Stop if Ranks converged
        if ranks_converged(current_ranks, previous_ranks):
            return current_ranks
        previous_ranks = current_ranks.copy()


def ranks_converged(new_ranks, old_ranks):
    for page in new_ranks:

        # New probability not calculated
        if not new_ranks[page]:
            return False

        # Difference to the nearest 1000th
        diff = new_ranks[page] - old_ranks[page]
        if round(diff, 4) > 0:
            return False
    return True


if __name__ == "__main__":
    main()
