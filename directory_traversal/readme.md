

It allows attacker to read files on the server that is running the application. Usually `passwd` file is used to exploit because it’s readable, and can be accessed during whatever the privilege the user has.

Impact:

1. C:- Allow you to read files on the system
2. I:- Some cases allow you to run commands and therefore alter files on the system.
3. A:- Similar to I, we can delete files which will become a case for the availability.

This exploit falls under injection cause it can help us (in rare cases) with remote code execution. Directory traversal is just one part of **********INJECTION.********** 

**How do you find it?**

Black Box Testing: 

1. Map the application
    1. Identify all instances where the web application appears to contain the name of a file or directory.
    2. Identify functions in the application whose implementation is likely to involve retrieval of data from server file system.
2. Test identified instances with common directory traversal payloads and observe how the application responds.
3. 

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/096330ba-6a79-4194-82c9-3d19ee71ae7b/95f74181-75e6-4335-833d-5a779093769d/Untitled.png)

1. Automate testing using a web application vulnerability scanner.

White Box Testing: 

1. Identify instances where user-supplied input is being passed to the file API or as parameters to the OS.
    1. Identify instances in a running application first and then review the code responsible for that functionality
    2. Grep on the functions in the code that are known to include and evaluate files on the server and review if they take user supplied input.
    3. User a tool to monitor all file system activity on the server. Then test each page of the application by inserting a single unique string. Set a filter in your monitoring tool for that specific string and identify all file system events that contain the string.
2. Validate potential directory traversal vulnerabilities on a running application.

**How to exploit?**

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/096330ba-6a79-4194-82c9-3d19ee71ae7b/b8b06c4d-688f-470b-8943-1bea9c5732f9/Untitled.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/096330ba-6a79-4194-82c9-3d19ee71ae7b/c28fabdf-62a8-48eb-9ec4-604c9ecf7882/Untitled.png)

**How to prevent?**

1. Avoid user input to file system API.
2. If that is unavoidable, two layers are needed:
    1. Validate user input by comparing it to an allow list of permitted values, if that’s not possible ensure the input only contains alphanumeric characters.
    2. After validating the user supplied input, use filesystem APU to canonicalize the path and verify that it starts with the expected base directory.
