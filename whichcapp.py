import whichcappreq as wc
import tkinter as tk


class WhichCapp:

    def __init__(self, master, api):
        self.master = master
        self.api = api
        self.city_array = []

        # Frame to manage search bar and button
        self.frame_search = tk.Frame(self.master, bg='blue', bd=5)
        self.frame_search.place(relx=0.01, rely=0.1, relheight=0.1, relwidth=0.98)

        # Search entry box
        self.entry_text = tk.Entry(self.frame_search, font=40)
        self.entry_text.place(relheight=1, relwidth=0.65, relx=0.1)

        # Search submit button
        self.submit_button = tk.Button(self.frame_search, text="Search", command=lambda: self.display_array(), font=40)
        self.submit_button.place(relheight=1, relx=0.76, relwidth=0.2)

        # Frame to display information
        self.frame_display = tk.Frame(self.master, bg='green')
        self.frame_display.place(relx=0.01, rely=0.25, relheight=0.7, relwidth=0.98)

        # Scroll bar for scrolling list box
        self.scroll_bar = tk.Scrollbar(self.frame_display)
        self.scroll_bar.place(relheight=0.98, relx=0.66, rely=0.01)

        # List box for displaying search results
        self.search_results = tk.Listbox(self.frame_display, yscrollcommand=self.scroll_bar.set, selectmode=tk.SINGLE,
                                         font=30)
        self.search_results.place(relheight=0.98, relwidth=0.65, relx=0.01, rely=0.01)
        self.search_results.bind('<<ListboxSelect>>', lambda event: self.display_information())
        self.scroll_bar.config(command=self.search_results.yview)

        self.cap_img = tk.Canvas(self.frame_display, bg='red')
        self.cap_img.place(relheight=0.98, relwidth=0.3, relx=0.69, rely=0.01)

    def display_array(self):
        self.search_results.delete(0, tk.END)
        self.city_array = self.api.search_city_name(self.entry_text.get())
        # Iterate through cities
        if self.city_array is not None:
            for i in self.city_array:
                self.search_results.insert(tk.END, str(i['title']))

    def which_hat(self, abbr):
        if abbr == 'sn':
            print("Wear Beanie")
        if abbr == 'sl':
            print("Wear Beanie")
        if abbr == 'h':
            print("Wear hat")
        if abbr == 't':
            print("Wear hat")
        if abbr == 'hr':
            print("Wear waterproof hat")
        if abbr == 'lr':
            print("Wear waterproof hat")
        if abbr == 's':
            print("No hat")
        if abbr == 'hc':
            print("wear hat")
        if abbr == 'lc':
            print("wear hat")
        if abbr == 'c':
            print("Wear hat")

    def display_information(self):
        index = self.search_results.curselection()[0]
        woeid = self.city_array[index]['woeid']
        abbr = self.api.get_weather(woeid)['consolidated_weather'][0]['weather_state_abbr']
        self.which_hat(abbr)


def main():
    """
    Initializes the GUI
    
    :return: None
    """
    WIDTH = 800
    HEIGHT = 600
    root = tk.Tk()
    api = wc.WeatherRequests()
    WhichCapp(root, api)
    root.title("Weather App")
    root.configure(width=WIDTH, height=HEIGHT)
    root.mainloop()


if __name__ == "__main__":
    main()
