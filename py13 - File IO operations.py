# File IO operations


# ------------writing operation
file1 = open("data.txt" , "a")
file1.write("My Name is Ved Prakash Gupta\n lets try to easy\n make a work easier\n ")
file1.close()n

# -----------Read Operation
f = open("data.txt" , "r+")
data = f.read()
print(data)

f.close()
"""
Hello My Name Is Ved Prakash gupta.
lets try to easy 
make a work easier
"""


f = open("data.txt" , "r+")
#data = f.read()

for line in f:
  print(line , end = "")
f.close()

"""
Hello My Name Is Ved Prakash gupta.
lets try to easy 
make a work easier
"""
"""
Let's take a look at some selected constants useful for detecting stream errors:

    errno.EACCES → Permission denied

    The error occurs when you try, for example, to open a file with the read only attribute for writing.

    errno.EBADF → Bad file number

    The error occurs when you try, for example, to operate with an unopened stream.

    errno.EEXIST → File exists

    The error occurs when you try, for example, to rename a file with its previous name.

    errno.EFBIG → File too large

    The error occurs when you try to create a file that is larger than the maximum allowed by the operating system.

    errno.EISDIR → Is a directory

    The error occurs when you try to treat a directory name as the name of an ordinary file.

    errno.EMFILE → Too many open files

    The error occurs when you try to simultaneously open more streams than acceptable for your operating system.

    errno.ENOENT → No such file or directory

    The error occurs when you try to access a non-existent file/directory.

    errno.ENOSPC → No space left on device

    The error occurs when there is no free space on the media.

The complete list is much longer (it includes also some error codes not related to the stream processing.)

"""
