# rhetoric

This project scrapes data from britishpoliticalspeech.org's speech archive. They have hundreds of speeches available and running speech_scraper.py will produce speeches.csv which is vital for creating the visuals. I then ran word_frequency.py to create an Excel that has the frequency of each word. I did some minor manipulation by hand to produce top_100_words_in_politics.xlsx which is used for create_plot1.py for example. You can then run create_plot[x for x in [1,3,4,5,6]] for each of those visuals. They are saved as plot[x for x in [1,3,4,5,6]]. For plot 2, I have used d3.js to create an interactive post where you can see the data more closesly when hovering over that column.

This can be summarised into the following steps:
1. Run speech_scraper.py
2. Run word_frequency.py
3. Manipulate frequency_by_party.xlsx to produce top_100_words_in_politics.xlsx
    a) This involves creating a table, sorting it, and deleting all but the top 100 lines.
    b) This would have been easy to write out programmatically but I didn't as the blog post only needs
       to be made once realistically and I wanted to devote more time to semantic analysis as I found
       it very interesting.
4. Run create_plot1.py
5. Run create_plot3.py
6. Run create_plot4.py
7. Run create_plot5.py
8. Run create_plot6.py
9. Since plot2 is contained in index.html, there is no code to 'run' as such. It is just directly referred to by the HackMD page.
