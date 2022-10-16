<p align="center">
  <a href="" rel="noopener">
 <img src="./assets/hackfest-cover.png" alt="Project logo"></a>
</p>
<h3 align="center">DermiTrack</h3>

<div align="center">


</div>

---

<p align="center"> A Simple tool for tracking your Skin related Diseases
    <br> 
</p>

## 📝 Table of Contents

- [📝 Table of Contents](#-table-of-contents)
- [🧐 Problem Statement <a name = "problem_statement"></a>](#-problem-statement-)
- [💡 Idea / Solution <a name = "idea"></a>](#-idea--solution-)
- [⛓️ Dependencies / Limitations <a name = "limitations"></a>](#️-dependencies--limitations-)
- [🚀 Future Scope <a name = "future_scope"></a>](#-future-scope-)
- [🏁 Getting Started <a name = "getting_started"></a>](#-getting-started-)
  - [Prerequisites](#prerequisites)
  - [Project Setup](#project-setup)
- [🎈 Usage <a name="usage"></a>](#-usage-)
- [⛏️ Built With <a name = "tech_stack"></a>](#️-built-with-)
- [✍️ Authors <a name = "authors"></a>](#️-authors-)

## 🧐 Problem Statement <a name = "problem_statement"></a>

The treatment of skin infections is a slow process, and it takes a long time for patients to see noticeable improvements in their condition. As a result, patients often become demotivated to continue treatment as they are unable to gauge how effective the treatment is. Patients who lose motivation often stop taking their medications which exacerbates the problem even more, resulting in an even longer recovery process.

## 💡 Idea / Solution <a name = "idea"></a>

Our app uses image processing to measure the spread of an infection in specific body parts of a patient currently undergoing recovery. The user can regularly take pictures of the effected area on a weekly or monthly basis and get a measurement of how much the area has been effected by the infection. Over time, the measurement of the infected area will be shown to decrease as the patient continues taking their medications. Patients will be shown a graph illustrating how each of their body parts effected by the infection have had their measurements decreased over time. Patients can look to this data as proof that their treatment is effective and gain motivation to continue taking their medication.

## ⛓️ Dependencies / Limitations <a name = "limitations"></a>

- Lack of Public Datasets for vitiligo and other diseases which results in depigmentation or hyperpigmentation of skin
- Describe each limitation in detailed but concise terms
- Explain why each limitation exists
- Provide the reasons why each limitation could not be overcome using the method(s) chosen to acquire.
- Assess the impact of each limitation in relation to the overall findings and conclusions of your project, and if
  appropriate, describe how these limitations could point to the need for further research.

## 🚀 Future Scope <a name = "future_scope"></a>

In the future we'd hope to gather a larger dataset to train more complex machine learning models and give patients more accurate measurements for their conditions. We'd also like to create a mobile app that people can buy so that they can take pictures using their phones and get their measurements done more easily.

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development
and testing purposes.

### Prerequisites

Install `pipenv` on your system

```
pip3 install pipenv
```

### Project Setup

To install project packages, navigate inside the project directory and

Run the following command:

```
pipenv install
```
this will install all the packages required to run this app on you machine

Create a `.env ` file and populate it with the environment variables present in `.env.template`

## 🎈 Usage <a name="usage"></a>

To start the project
1. Activate the Pipenv virtual environment using:
   ```
   pipenv shell
   ```
2. Run the streamlit app using:
   ```
   streamlit run Authenticate_User.py
   ```

## ⛏️ Built With <a name = "tech_stack"></a>

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/) 
- [OpenCV](https://opencv.org/) 
- [rembg](https://github.com/danielgatis/rembg) 
- [SQLite](https://www.sqlite.org/index.html) 
  
## ✍️ Authors <a name = "authors"></a>

- [@hussainfolio3](https://github.com/hussainfolio3)
- [@muhammadanas25](https://github.com/muhammadanas25)
- [@RizwanNiaz](https://github.com/RizwanNiaz)
- [@MuhammadRafay151](https://github.com/MuhammadRafay151)
