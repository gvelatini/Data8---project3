# Data 8 Private Materials for Spring 2020
This repo contains the public and private materials that were used in the Data 8 Foundations of Data Science course during the Spring 2020 semester.

This includes: homeworks, lab notebooks, projects, lecture notebooks + slides, worksheets, solutions + private auto-grader tests, and other reference material.

**PLEASE DO NOT SHARE THE CONTENTS OF THIS REPO WITH ANYONE.**

## Confidentiality Agreement

In order to use the contents of this repo in your course, you must agree and sign [this](https://docs.google.com/document/d/1ahVCqY_jAQymDmsS_lqHYTgEigI5ZoT6tQFFN5Vbz5E/edit) privacy form and email it back to [ds-help@berkeley.edu](ds-help@berkeley.edu).

Since these assignments are used across institutions teaching data science, it is imperative that **none of the assignments' private tests or solutions should become accessible to students**.
When distributing assignments, instructors should create a separate public repository with blank assignment files and public tests. 
For example, [this](https://github.com/data-8/materials-sp20) repository was the public version of the material given to Berkeley students in spring 2020. 
You can distribute assignments using [`nbgitpuller`](http://nbgitpuller.link/) if you are using a JupyterHub, or through your Learning Management System as a folder of files if students are doing data science locally.

Private tests should never leave your computer, except being uploaded to Gradescope through otter's assignment generation.


## Autograding

All assignments and tests have been modified to use [otter grader](https://otter-grader.readthedocs.io/en/beta/). 
Otter was developed by UC Berkeley's Data Science Education Program as a more adoptable autograding solution. 
To grade assignments, you can set up otter to run locally on your computer or with gradescope's autograding system.

For each assignment, comprehensive tests (including hidden tests) and public tests have been separated into folders, `autograder_tests` and `tests`, respectively. 
You will need to specify both directories when generating an assignment for otter. 

If you decide to augment the assignments and need to write new test cases, check out the documentation on writing ok test files [here](https://otter-grader.readthedocs.io/en/beta/test_files.html).

## Useful Links

- The `8X_youtube_videos.csv` file contains a table of unlisted youtube videos of Data 8 made for our [edX course](https://www.edx.org/professional-certificate/berkeleyx-foundations-of-data-science). The videos are created and recorded by Ani Adhikari, John Denero, and David Wagner. You can use these videos to get a better sense of the pedagogy and delivery of Data 8 by the original course facilitators.
- Make sure to check out the [Data Science Education Resources](https://data.berkeley.edu/external) home page for a list of all resources available in teaching data science.
- [The Data Science Educator's Guide to Technology Infrastructure](https://ucbds-infra.github.io/ds-course-infra-guide/intro.html) is useful for all infrastructure related information, an includes information on autograding and JupyterHub.
- The [Zero to Data 8 Guide](http://data8.org/zero-to-data-8/) goes over the pedagogical side of teaching Data 8, based on Berkeley's experiences in running the course.
