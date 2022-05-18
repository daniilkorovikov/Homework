class Pagination():

    def __init__(self, text, page_items):
        self.text = text
        self.page_items = page_items
        self.res = []
        start = 0
        stop = page_items
        while start < len(self.text):
            self.res.append(self.text[start:stop])
            start += page_items
            stop += page_items

    def page_count(self):
        print((len(self.text) + 1) // self.page_items)

    def item_count(self):
        print(len(self.text))

    def count_items_on_page(self, index):
        try:
            print(len(self.res[index]))
        except Exception:
            print('Exception: Invalid index. Page is missing.')

    def display_page(self, index):
        try:
            print(self.res[index])
        except Exception:
            print('Exception: Invalid index. Page is missing.')

    def find_page(self, seq):
        if self.text.count(seq) > 0:
            page_list = []
            ind = -1
            for i in range(self.text.count(seq)):
                ind = self.text.find(seq, ind + 1)
                if ind // self.page_items == (ind + len(seq)) // self.page_items:
                    page_list.append(ind // self.page_items)
                else:
                    page_list.append(ind // self.page_items)
                    page_list.append((ind // self.page_items) + 1)
                print(page_list)
        else:
            print(f'Exception: {seq} is missing on the pages')


pages = Pagination('Your beautiful text', 5)
pages.page_count()
pages.item_count()
pages.count_items_on_page(0)
pages.count_items_on_page(3)
pages.count_items_on_page(4)
pages.find_page('Your')
pages.find_page('e')
pages.find_page('beautiful')
pages.find_page('great')
pages.display_page(0)
