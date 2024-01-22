# Lab 2: Basic Linux Commands



## Prerequisites

You should have made yourself familiar with the ‘Linux Commands’ content section. It will be helpful to have this open as a reference while you work through the lab.

Be sure to do steps in order, remember where you leave off if you must do things in more than one sitting.

## Objectives

·    Practice the use of basic Linux commands



## Task 1

`ssh` into the PI and create the following directory structure starting at /home/pi. Remember /home/pi is the directory you are brought into by default when you log in (Home Directory). Remember also that Linux is case sensitive.

It is highly advised you keep a notepad open and put in every command you used to create this folder structure. Task 2 will require you to use Python to do the same thing programmatically.

![Screen Shot 2021-01-11 at 5.18.19 PM](/Users/jeromemizon/Documents/8254/21W/tree.png)

Now, from a terminal type in the following. Be sure you are in your home directory (`/home/pi`)

 `ls -l > lab2-1.txt`       

 **Question 1a: What does this do?**



Make a copy of the file `lab2-1.txt` and call it `lab2-2.txt`

**Question 1b: What command did you use?**



Using Nano, change one of the lines of `lab2-2.txt` then save the file.                           

Move the file `lab2-1.txt` to the folder `cst8254/linux/labs/Lab2`

**Question 1c: What command did you use?**



Copy the file `lab2-2.txt` to the folder `cst8254/linux/labs/Lab2`

**Question 1d: What Command did you use?**

 

Using Nano, create the file `<networkid>.txt` in the `cst8254` folder where `<networkid>` is your Algonquin network ID. As for the content of the file, write a simple one liner on one thing you learned about Linux this semester.

Once you have saved and exited from Nano, issue the following command:

`tree cst8254 > lab2-3.txt`       



### Task 2:

Create a gzipd tar archive of the directory structure using. 

 `tar zcvf /home/pi/<networkid>-lab2.tgz /home/pi/cst8254       `

Run a terminal, make sure your present working directory is your desktop and do the following.

 `sftp  pi@<your-ip-or-host>  get <networkid>-lab3.tgz    `

 

### Task 3:

Delete the `cst8254` folder form you Pi then write a python program that makes use of the `os` and `shutil `modules to recreate the same folder structure. Name your program `lab2.py`



### Submission

 Please submit the following files to GitHub 

·    `<networkid>-lab2.tgz`

·    `<networkid>-answers.md`

·    `lab2.py`

