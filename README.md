# Easy Split
Simple and powerfull python script to easily split your data into traning and validation (for deep learning projects). Works in binary and multiclass classification.

# How it works ?
This script can be useful if you want to use keras ImageGenerator `flow_from_directory`. This script can create `train` and `valid` folder using class folder

```
└───data
    ├───class_1
    │       example_0.txt
    │       example_1.txt
    │       example_2.txt
    │       example_3.txt
    │       example_4.txt
    │       example_5.txt
    │       example_6.txt
    │       example_7.txt
    │       example_8.txt
    │       example_9.txt
    │
    └───class_2
            example_0.txt
            example_1.txt
            example_2.txt
            example_3.txt
            example_4.txt
            example_5.txt
            example_6.txt
            example_7.txt
            example_8.txt
            example_9.txt
```

And turn it into this. By default the validation size is 20% but you can tweak the script as you want.

```
└───dataset
    ├───train
    │   ├───class_1
    │   │       example_2.txt
    │   │       example_3.txt
    │   │       example_4.txt
    │   │       example_5.txt
    │   │       example_6.txt
    │   │       example_7.txt
    │   │       example_8.txt
    │   │       example_9.txt
    │   │
    │   └───class_2
    │           example_2.txt
    │           example_3.txt
    │           example_4.txt
    │           example_5.txt
    │           example_6.txt
    │           example_7.txt
    │           example_8.txt
    │           example_9.txt
    │
    └───valid
        ├───class_1
        │       example_0.txt
        │       example_1.txt
        │
        └───class_2
                example_0.txt
                example_1.txt
```
