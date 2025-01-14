Week 3 summary

Author: Wenhua Zhou(wz2812@ic.ac.uk)

Date: 14/10~~20/10

Chapter covered: Biological Computing in R, Data management

Status: chapter covered and practicals all done

###############################################################

Chapter 7: Biological Computing in R

Code directory:

basic_io.R
# A simple script to illustrate R input-output

control_flow.R
# if, then, else and some for and while loops example

break.R
# loop with break statement

next.R
# loop with next statement

boilerplate.R
# A boilerplate R script with R functions

TreeHeight.R
# work for practicals
# originally is a function calculate the tree height
# now is modified to load data from trees.csv to calculate all tree heights in the data
# save the results into Results directory that contains
# both original data and the calculate tree height in the given format

preallocate.R
# example of the computational difference between not-allocated and pre-allocated vector loop

apply1.R
# example of apply functions

apply2.R
# example of another apply functions

sample.R
# example of vectorization involving lapply and sapply

Ricker.R
# function of a simple Ricker model with a simple plot

Vectorize1.R
# example of computational difference between for loops and in-built vectorized function

Vectorize1.py
# python version of Vectorize1.R
# use numpy to create matrix and calculate sum

Vectorize2.R
# R practicals
# given a function for Ricker equation with gaussian fluatuations
# improve the given function speed by vectorization

Vectorize2.py
# python version of Vectorize2.R
# use list comprehension to vectorize

run_vectorize.sh
# the shell script used to run the 4 Vectorized file in terminal
# compute the results in terminal and include a brief summary

try.R
# example of try function

browse.R
# example of browser() function for debugging and trackback

TAutoCorr.R
# R practicals
# read data of temperature in a time series
# compute correlation and p-value

TAutoCorrSummary.tex
# R practicals
# source code of pdf latex conclusion of TAutoCorr.R

get_TreeHeight.R
# R practicals
# take a csv file name from the command line
# output the same results as TreeHeight.R with different name

run_get_TreeHeight.sh
# R practicals
# shell scripts to run_get_TreeHeight.R with Trees data, use trees.csv as example

get_TreeHeight.py
# R practical:
# The python version of get_TreeHeight.R, get the tree height and write
# as a csv file run by run_get_TreeHeight.sh


Data directory:

trees.csv 
# downloaded data for trees 

KeyWestAnnualMeanTemperature.Rdata
# R data with annual mean temperature for autocorrelation practicals


Results directory:

MyData.csv
# saved results of trees.csv data

TreeHts.csv
# R practicals results
# save the results of trees.csv data including the calculated tree height

TAutoCorr_Summary.pdf
# R practicals results
# the pdf ducument written in LaTeX interpret the results of correlation

treeheight_py.csv
# R practicals results
# save the results from get_TreeHeight.py using python and script run_get_TreeHeight.sh

trees_treeheights.csv
# R practicals results
# save the results from get_TreeHeight.R takes a csv file name from the command line

########################################

Chapter 8: Data management, exploration and visualization

Code directory:

DataWrang.R
# R script wrangling the given data from PoundHillData.csv

DataWrangTidy.R
# R practicals
# use dplyr and tidyr to wrangle data

PP_Lattice.R
# R practicals
# output 3 pdf files of lattice graphs
# calculate mean and median by feeding type

Girko.R
# Plot two dataframes by Girko's circular law

MyBars.R
# example of annotating plots

plotLin.R
# example of mathematical display

PP_Regress.R
# R practicals
# output the given figure 
# do linear regression of predator type
# write csv of linear regression data

GPDD_Data.R
# R practicals
# use maps package to map

PP_Regress_loc.R
# R practicals
# write a csv of the same in PP_Regress with one more filter location


Data directory:

PoundHillData.csv
# pound hill data downloaded from repository

PoundHillMetaData.csv
# pound hill data file name and description downloaded from repository

EcolArchives-E089-51-D1.csv
# Ecological Archives data downloaded from repository

Results.txt
# downloaded data for annotating plots

PGDDFiltered.Rdata
# downloaded data for maps package to plot maps



Results directory:

Pred_Prey_Overlay.pdf
# saved graphic of an example plot

Pred_Lattice.pdf
# R practicals
# lattice graph of predator mass in logarithms

Prey_Lattice.pdf
# R practicals
# lattice graph of prey mass in logarithms

SizeRatio_Lattice.pdf
# R practicals
# lattice graph of size ratio in logarithms

MyFirst-ggplot2-Figure.pdf
# example of saving plot

Girko.pdf
# saved result figure of Girko.R

MyBars.pdf
# saved result figure of MyBars.R

MyLinReg.pdf
# saved result figure of plotLin.R

PP_Regress.pdf
# R practicals
# saved result of the ggplot from PP_Regress.R

PP_Results.csv
# R practicals
# saved mean and median log predator mass, prey mass, and size ratio
# by feeding type

PP_Regress_Results.csv
# R practical results
# saved csv file of linear regression data to different
# feeding type and life stage combination

PP_Regress_loc_Results.csv
# R practical results
# saved csv file of linear regression data to different
# feeding type, life stage and location combination
