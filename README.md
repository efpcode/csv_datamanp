# CSV Data Manipulator (csv\_datamanp)
This was created to facilitate data manipulation, data filtering and lastly data mapping
when working with response data from a service.

Current workflow, is to manipulate data directly via software that is cell or table based and this is not an optimal
solution. Since every operation is made by a human, and human makes mistakes, humans might not share procedures and humans 
are bad at verifying the results after an operation has been carried out.  

So to streamline the process i.e. removing the human factor from these operations we can achieve a more fluid way
of dealing with large amount of data and also test and expect certain outcomes when doing so.  


## The Pros of Automatizing Data Pipelines
* The greatest gain is in time, a task that might take between 5-10 minutes can be reduced to mere seconds.
* Consist work pace, procedure is not dependent on the users knowledge of the software or the familiarity of a certain software. 
* Work quality consistence, meaning that actions carried via a script is not altered during an action like e.g. copy/paste action or other human mishaps. 
* Verification a good in-house scripting solution should be covered by certain set tests and be limited to solve well define issue.

## The Cons of Automatizing Data Pipelines
* Code and additional library dependency/cies.
* Bus factor i.e. the amount of people that could understand and edit/maintain the code base, carries out automation.  
* Overestimating gain of automatizing task, not all problems are meant to be sent through pipeline and one should think twice before starting code a solution. 

Now that we have covered the caveats for this project we can start to code, what I believe to be simple enough issues and should result 
in great gains.

## The issues
* Removing none alphanumeric characters from a data set i.e. only allow 0-9 and letters. 
* Map old user identity to another identity, think dictionary key value paris.
* Subset a pool of user from a larger set of data. 

# Python + Pandas = Data Science Tool
This will not come as a surprise that programing language is Python and that the additional 
library is Pandas. Both are used ubiquitously in the data science community and are often paired with other languages 
as R, matlab etc. 

The reason for picking Python is the readability aspect of the syntax that would be lighter to digest than other programing 
languages for none coders/programmers.

The reason for Pandas, is that its fairly mature library and would suffice for most use cases as complement to software
used currently in-house. 

# Limitations
This will be command line driven project, since this is a hobby build and for a more user-friendly version i.e. GUI, I 
would need to dedicate more time and the effort.
