"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": "/a/",
            "answer": "/a"
        },{
            "input": "/a/b",
            "answer": "/a/b"
        },{
            "input": "/a//b/c",
            "answer": "/a/b/c"
        },{
            "input": "/a/b/./ci",
            "answer": "/a/b/ci"
        },{
            "input": "/a/b/../c",
            "answer": "/a/c"
        },{
            "input": "/a/b//",
            "answer": "/a/b"
        },{
            "input": "a/../b/c",
            "answer": "b/c"
        },{
            "input": "vi/..",
            "answer": "."
        },{
            "input": "./.",
            "answer": "."
        },{
            "input": "/for/../..",
            "answer": "/"
        },{
            "input": "/for/../../no/..",
            "answer": "/"
        },{
            "input": "for/../..",
            "answer": ".."
        },{
            "input": "../foo",
            "answer": "../foo"
        }
        
    ],
    "Extra": [
        {
            "input": "/a/v/c",
            "answer": "/a/v/c"
        },{
            "input": "/mix/max/../num/../vim",
            "answer": "/mix/vim"
        },{
            "input": "/../a/big",
            "answer": "/a/big"
        },{
            "input": "/../../v1//",
            "answer": "/v1"
        },{
            "input": "fr/mi/././hy",
            "answer": "fr/mi/hy"
        },{
            "input": "/ft/g.t/ft..gy/f..g..t/",
            "answer": "/ft/g.t/ft..gy/f..g..t"
        },{
            "input": "/",
            "answer": "/"
        },{
            "input": ".././..",
            "answer": "../.."
        },{
            "input": "../foo/../foo",
            "answer": "../foo"
        },{
            "input": "/../foo/../foo",
            "answer": "/foo"
        },{
            "input": "///",
            "answer": "/"
        },{
            "input": "///d",
            "answer": "/d"
        },{
            "input": "////",
            "answer": "/"
        },{
            "input": "////d",
            "answer": "/d"
        },{
            "input": "//foo//goo",
            "answer": "/foo/goo"
        },{
            "input": "foo/./.",
            "answer": "foo"
        },{
            "input": "/.../....",
            "answer": "/.../...."
        }
    ]
}
