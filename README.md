# Python-Text-To-Speech
> An interactive command-line tool for text-to-speech (TTS) synthesis using both eSpeak and Piper TTS engines.

---

## Features

* **Dual Engine Support:** Switch seamlessly between the fast, robotic **eSpeak** engine and the realistic, neural **Piper TTS** engine.
* **Interactive CLI:** An easy-to-use command-line interface for controlling all features.
* **Advanced Speech Customization (eSpeak):** Adjust rate, pitch, amplitude, word gap, and select from various voice variants.
* **High-Quality Speech Synthesis (Piper):** Leverages a modern neural network model for natural, human-like speech.
* **Play & Save Functionality:** Speak text directly and simultaneously save the output to a timestamped `.wav` file with a single command.

---

> ###### Dependencies
> (This script is designed to run in a **Linux or WSL (Windows Subsystem for Linux)** environment.)
>
> Required for the speech engines. Open your terminal and run the appropriate command:
> 
> * **For Fedora/CentOS:**
`sudo dnf install espeak-ng`
>
> * **For Debian/Ubuntu:**
`sudo apt-get install espeak-ng`
>
> ###### Python Libraries
> `pip install pyttsx3 piper-tts`
>
>
<details>
  <summary>Python Install Tutorial</summary>

> ### [Python Installation Guide](https://www.youtube.com/watch?v=ddGTXBhaGWA)
> #### [@Amit.Thinks](https://www.youtube.com/@Amit.Thinks)
> 
>  <a href="https://www.youtube.com/watch?v=ddGTXBhaGWA">
> <div align="center">
>
>  https://github.com/user-attachments/assets/f069793d-8245-4164-aaeb-631a388f9df3
>  </div>
>
> In this video, learn to download and install Python 3.13.5 on Windows 11. We will also run a sample Python code.
>
>
> Python Tutorial (English): https://bit.ly/3znnb1y
>
> Python Tutorial (Hindi): https://youtu.be/b97WsOM9BYg
>
> Python Study Material: https://studyopedia.com/tutorials/python3/
> 
> Google Colab Tutorial: https://youtu.be/iMlMfrXJYSg
> 
> Anaconda Tutorial: https://youtu.be/ovlID7gefzE
> 
> Jupyter Notebook Tutorial: https://youtu.be/Ou-7G9VQugg
> 
> PyCharm Tutorial: https://youtu.be/nixcq6mEGWQ
> 
> Pandas Tutorial (English): https://youtu.be/yFoVs3_wvPo
> 
> Pandas Tutorial (Hindi): https://youtu.be/57POFzZ7f60
> 
> NumPy Tutorial (English): https://youtu.be/WsENswmSz6M
> 
> NumPy Tutorial (Hindi): https://youtu.be/roqStVWNR7Q
> 
> Matplotlib Tutorial (English): https://youtu.be/DFBkTIhptOQ
> 
> Matplotlib Tutorial (Hindi): https://youtu.be/vBCXsAd_swk
> 
> #Python #Windows #installation
> -------------------------------------------------------------------------------
> 
> ✔️My Website - https://studyopedia.com
> 
> ✔️Join Us at 59/month: https://bit.ly/3WV9sXK
> 
> ✔️Data Analytics Tutorial: https://bit.ly/48MxVTU
> 
> ✔️Web Dev Tutorial: https://bit.ly/3tl9nlp
> 
> ✔️Free Study Material: https://bit.ly/3K7lzbP
> 
> 👉  Follow me
> LinkedIn - https://bit.ly/3C1CY4v
> Instagram - https://bit.ly/3z8Fg1d
> ---------------------------------------------------------------------------------
> 
> Tableau Tutorial⭐️https://youtu.be/4aTvjpdOMT4
> 
> Power BI Tutorial⭐️https://youtu.be/OITCW7ETz-M
> 
> Generative AI Course (English)⭐️https://bit.ly/3Vhsbxv
> 
> Generative AI Course (Hindi) ⭐️ https://bit.ly/3V76ZKp
> 
> Python Tutorial (English)⭐️ https://youtu.be/HakXpkXcjdI
> 
> Python Tutorial (Hindi)⭐️ https://youtu.be/b97WsOM9BYg
> 
> Pandas Tutorial (English)⭐️https://youtu.be/yFoVs3_wvPo
> 
> Pandas Tutorial (Hindi)⭐️https://youtu.be/57POFzZ7f60
> 
> NumPy Tutorial (English)⭐️https://youtu.be/WsENswmSz6M
> 
> NumPy Tutorial (Hindi)⭐️https://youtu.be/roqStVWNR7Q
> 
> Matplotlib Tutorial (English)⭐️https://youtu.be/DFBkTIhptOQ
> 
> Matplotlib Tutorial (Hindi)⭐️https://youtu.be/vBCXsAd_swk
> 
> Google Colab Tutorial ⭐️https://youtu.be/iMlMfrXJYSg
> 
> Anaconda Tutorial ⭐️ https://youtu.be/ovlID7gefzE
> 
> PyCharm Tutorial ⭐️https://youtu.be/nixcq6mEGWQ
> 
> SQL Tutorial ⭐️https://youtu.be/7dcYlJcGhqk
> 
> MySQL Tutorial⭐️https://youtu.be/sgpDAiF-18o
> 
> MySQL Workbench Tutorial: https://youtu.be/UzodkZUt5JY
> 
> HTML Tutorial ⭐️https://bit.ly/3VHaUvq
> 
> jQuery Tutorial (English)⭐️https://youtu.be/5BTWmXFOKlc
> 
> jQuery Tutorial (Hindi)⭐️https://youtu.be/bvmAsDvQ1NM
> 
> Bootstrap Tutorial⭐️https://youtu.be/nahewStckVU
> 
> ►  Programming - Free Study Material (Downloadable)
> 
> Machine Learning⭐️ https://studyopedia.com/tutorials/machine-learning
> 
> Deep Learning⭐️https://studyopedia.com/tutorials/deep-learning
> 
> Tableau ⭐️https://studyopedia.com/tutorials/tableau
> 
> Power BI ⭐️https://studyopedia.com/tutorials/power-bi
> 
> Python ⭐️https://studyopedia.com/tutorials/python3
> 
> Numpy ⭐️https://studyopedia.com/tutorials/numpy
> 
> Pandas ⭐️https://studyopedia.com/tutorials/pandas
> 
> Matplotlib ⭐️https://studyopedia.com/tutorials/matplotlib
> 
> Java ⭐️https://studyopedia.com/tutorials/java
> 
> C ⭐️https://studyopedia.com/tutorials/c-programming
> 
> C++ ⭐️https://studyopedia.com/tutorials/cpp/
> 
> C# ⭐️https://studyopedia.com/tutorials/csharp/
> 
> Android ⭐️https://studyopedia.com/tutorials/android
> R ⭐️https://studyopedia.com/tutorials/r-tutorial
> 
> Bootstrap⭐️https://studyopedia.com/tutorials/bootstrap/
> 
> HTML5 ⭐️https://studyopedia.com/tutorials/html5
> 
> JavaScript⭐️https://studyopedia.com/tutorials/javascript/
> 
> jQuery⭐️https://studyopedia.com/tutorials/jquery/
> 
> ►  Database  - Free Study Material (Downloadable)
> SQL ⭐️https://studyopedia.com/tutorials/sql
> 
> MySQL ⭐️https://studyopedia.com/tutorials/mysql
> 
> MongoDB⭐️https://studyopedia.com/tutorials/mongodb
> 
> Python🔥https://studyopedia.com/java/java-interview-questions-and-answers
> 
> Java 🔥https://studyopedia.com/python3/python-multiple-choice-questions/
> 
> Android🔥https://studyopedia.com/android/android-interview-questions/
> 
> ReactJS🔥https://studyopedia.com/reactjs/react-interview-questions
> 
> Bootstrap 🔥https://studyopedia.com/bootstrap/bootstrap-interview-questions
> 
> SQL 🔥https://studyopedia.com/sql/sql-interview-questions
> 
> MongoDB 🔥https://studyopedia.com/mongodb/mongodb-interview-questions
> 
> MySQL 🔥https://studyopedia.com/mysql/mysql-interview-questions
> 
> 👉 About Amit Thinks YouTube Channel
> I am Amit Diwan, a self-made Entrepreneur, running "Amit Thinks", a Tech YouTube Channel. Also running an E-Learning website "[studyopedia.com](https://studyopedia.com)".  We publish videos in  English and Hindi on Programming, Databases, and Web Dev Technologies. I have left a job offer from Accenture and 3 government jobs to follow my dream of being an
> entrepreneur.
>
> Join this channel to get access to the perks:
> https://www.youtube.com/channel/UCgnr2Lkl1LZf0IOKRDAoJ2g/join
>
> ►  Subscribe
> https://www.youtube.com/@Amit.Thinks/
</details>



<details>
  <summary>Misc Info</summary>

![Star History Chart](https://api.star-history.com/svg?repos=Zwarb/Python-Text-To-Speech&type=Date)

###### This project was made with AI.
