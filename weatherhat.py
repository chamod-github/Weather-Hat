import weatherhatreq as whr
import tkinter as tk
from PIL import Image, ImageTk


class WeatherHat:
    """

    Handles GUI related tasks of Weather Hat

    """

    def __init__(self, master, api):
        """

        Initialize the WeatherHat GUI

        :param master: Main tkinter window
        :param api: API object
        """
        self.master = master
        self.api = api
        self.city_array = []

        # Frame to manage search bar and button
        self.frame_search = tk.Frame(self.master, bd=5)
        self.frame_search.place(relx=0.01, rely=0.1, relheight=0.1, relwidth=0.98)

        self.entry_text = tk.Label(self.frame_search, font=40, text="Enter City: ")
        self.entry_text.place(relheight=1, relwidth=0.1, relx=0.01)

        # Search entry box
        self.entry_text = tk.Entry(self.frame_search, font=40)
        self.entry_text.place(relheight=1, relwidth=0.5, relx=0.15)

        # Press enter to populate search results
        self.master.bind('<Return>', lambda event: self.display_array())

        # Search submit button
        self.submit_button = tk.Button(self.frame_search, text="Search", command=lambda: self.display_array(), font=40)
        self.submit_button.place(relheight=1, relx=0.66, relwidth=0.2)

        # Frame to display information
        self.frame_display = tk.Frame(self.master, bg='#000050')
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

        # Frame that holds weather info widgets
        self.cap_info = tk.Frame(self.frame_display, bg='#000050')
        self.cap_info.place(relheight=0.98, relwidth=0.3, relx=0.69, rely=0.01)

        # Default placeholder image
        self.img_var = ImageTk.PhotoImage(Image.open("images/default_hat.png"))

        # Cap info image canvas
        self.cap_img = tk.Label(self.cap_info, bg='#000050')
        self.cap_img.place(relheight=0.5, relwidth=0.98, relx=0.01, rely=0.01)

        # Cap info message
        self.weather_var = tk.StringVar()
        self.info_text = tk.Message(self.cap_info, textvariable=self.weather_var, anchor=tk.N, padx=20, pady=20,
                                    justify=tk.LEFT)
        self.info_text.place(relheight=0.47, relwidth=0.98, relx=0.01, rely=0.52)

    def display_array(self):
        """

        Sets the search results list box to search results returned from the API

        :return: None
        """

        self.search_results.delete(0, tk.END)
        self.city_array = self.api.search_city_name(self.entry_text.get())

        # Iterate through cities and  insert them to the list box
        if self.city_array is not None:
            for i in self.city_array:
                self.search_results.insert(tk.END, str(i['title']))

    def which_hat(self, abbr):
        """

        Sets the information text and image based on the weather abbreviation

        :param abbr: Abbreviation letters of the weather condition
        :return: None
        """
        if abbr == 'sn':
            self.weather_var.set("It is snowing. You need a snow hat!")
            self.update_hat_img("images/snow_hat_heavy_snow.png")
            return
        if abbr == 'sl':
            self.weather_var.set("There is sleet. You need a light snow hat!")
            self.update_hat_img("images/snow_hat_light_snow.png")
            return
        if abbr == 'h':
            self.weather_var.set("There is hail. You need a hard hat!")
            self.update_hat_img("images/hard_hat.png")
            return
        if abbr == 't':
            self.weather_var.set("There is a thunderstorm. You need a hat without metal!")
            self.update_hat_img("images/brim_hat_no_metal.png")
            return
        if abbr == 'hr':
            self.weather_var.set("It is heavily raining. You need a waterproof hat with a brim!")
            self.update_hat_img("images/brim_hat_heavy_rain.png")
            return
        if abbr == 'lr':
            self.weather_var.set("It is lightly raining. You need a hat with a brim!")
            self.update_hat_img("images/brim_hat_light_rain.png")
            return
        if abbr == 's':
            self.weather_var.set("It is showering. You need a hat with a brim!")
            self.update_hat_img("images/brim_hat_light_rain.png")
            return
        if abbr == 'hc':
            self.weather_var.set("It is heavy cloudy. You can wear any hat!")
            self.update_hat_img("images/brim_hat.png")
            return
        if abbr == 'lc':
            self.weather_var.set("It is light cloudy. You can wear any hat!")
            self.update_hat_img("images/brim_hat.png")
            return
        if abbr == 'c':
            self.weather_var.set("It is clear. You can wear any hat!")
            self.update_hat_img("images/brim_hat.png")
            return
        else:
            self.weather_var.set("information not available.")
            self.update_hat_img("images/default_hat.png")
            return

    def update_hat_img(self, image_name):

        self.img_var = ImageTk.PhotoImage(Image.open(image_name))
        self.cap_img.configure(image=self.img_var)

    def display_information(self):
        """

        Gets the current selected search result of the list box and finds the corresponding information
        about it.

        :return: None
        """
        selection = self.search_results.curselection()
        # an option must be selected
        if selection:
            # Find the index of the selected result
            index = selection[0]
            woeid = self.city_array[index]['woeid']

            # Get the corresponding weather abbreviation
            abbr = self.api.get_weather_abbr(woeid)
            self.which_hat(abbr)


def main():
    """
    Initializes the GUI
    
    :return: None
    """
    WIDTH = 800
    HEIGHT = 600
    root = tk.Tk()
    api = whr.WeatherHatRequests()
    WeatherHat(root, api)
    root.title("Weather App")
    root.configure(width=WIDTH, height=HEIGHT)
    root.resizable(False, False)
    root.mainloop()


if __name__ == "__main__":
    main()
