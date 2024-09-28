# from random import choice, randint
#
#
# def get_response(user_input: str, https=None) -> str:
#     lowered: str = user_input.lower()
#     keywords: list[str] = user_input.lower().strip().split()
#
#     if lowered == "":
#         return "Well, I can't respond to nothing, can I?"
#     elif lowered == "hi":
#         return "Hello bbg!"
#     elif lowered == "bye":
#         return "Goodbye bbg!"
#     elif lowered == "roll dice":
#         return f"You rolled a {randint(1, 6)}!"
#     elif lowered == "flip a coin":
#         return choice(["Heads!", "Tails!"])
#     elif lowered == "how are you":
#         return "I'm doing fine bbg, tell me about yourself!"
#
#     # redirecting to language specific resources
#
#     # cpp
#     elif ("cpp" or "c++") and ("resources" or "resource") in keywords:
#         return f"C++ is a general-purpose programming language created by Bjarne Stroustrup as an extension of the C programming language, or 'C with Classes'. For specific resources, refer here - {https://discord.com/channels/781467057807032323/1035869217074978886}"
#     # python
#     elif "python" and ("resources" or "resource") in keywords:
#         return f"Python is an interpreted, high-level and general-purpose programming language. For specific resources, refer here - {https://discord.com/channels/781467057807032323/1035869711004618834}"
#     # java
#     elif "java" and ("resources" or "resource") in keywords:
#         return f"Java is a class-based, object-oriented programming language that is designed to have as few implementation dependencies as possible. For specific resources, refer here - {https://discord.com/channels/781467057807032323/1045022001762418779}"
#     # javascript
#     elif ("javascript" or "js") and ("resources" or "resource") in keywords:
#         return f"JavaScript is a high-level, interpreted programming language that conforms to the ECMAScript specification. For specific resources, refer here - {https://discord.com/channels/781467057807032323/1045027084717797436}"
#     # golang
#     elif ("golang" or "go") and ("resources" or "resource") in keywords:
#         return f"Go is a statically typed, compiled programming language designed at Google. For specific resources, refer here - {https://discord.com/channels/781467057807032323/1192175876213833799}"
#     # rust
#     elif "rust" and ("resources" or "resource") in keywords:
#         return f"Rust is a multi-paradigm system programming language focused on safety, especially safe concurrency. For specific resources, refer here - {https://discord.com/channels/781467057807032323/1038338641421938738}"
#     # typescript
#     elif ("typescript" or "ts") and ("resources" or "resource") in keywords:
#         return f"TypeScript is an open-source language which builds on JavaScript, one of the world’s most used tools, by adding static type definitions. For specific resources, refer here - {https://discord.com/channels/781467057807032323/1247558205165535383}"
#     # clean code
#     elif ("clean" and "code") and ("resources" or "resource") in keywords:
#         return f"Clean code is code that is easy to understand and easy to change. For specific resources, refer here - {https://discord.com/channels/781467057807032323/1185484608205238332}"
#     # computer science basics
#     elif ("cs" and "basics") and ("resources" or "resource") in keywords:
#         return f"Computer Science basics are the foundation of computer science. For specific resources, refer here - {https://discord.com/channels/781467057807032323/1251496416203903027}"
#
#     # redirecting to domain specific resources
#
#     # System (Linux) Programming
#     elif ("system" and "programming" and "linux") and (
#         "resources" or "resource"
#     ) in keywords:
#         return f"System programming is the activity of programming computer system software. For specific resources, refer here - {https://discord.com/channels/781467057807032323/1108712976971730956}"
#     # Web Development
#     elif (("web" and "development") or ("web" and "dev") or "html" or "css") and (
#         "resources" or "resource"
#     ) in keywords:
#         return f"Web development is the work involved in developing a website for the Internet. For specific resources, refer here - {https://discord.com/channels/781467057807032323/1035874106605842553}"
#     # App Development
#     elif (
#         ("app" and "development") or ("app" and "dev") or "android" or "ios" or "app"
#     ) and ("resources" or "resource") in keywords:
#         return f"App development is the process of creating a mobile application. For specific resources, refer here - {https://discord.com/channels/781467057807032323/1035874202886086657}"
#     # flutter
#     elif "flutter" and ("resources" or "resource") in keywords:
#         return f"Flutter is an open-source UI software development kit created by Google. For specific resources, refer here - {https://discord.com/channels/781467057807032323/1176525373148774501}"
#     # DSA
#     elif (
#         "dsa"
#         or ("data" and "structures")
#         or "algorithms"
#         or "ps"
#         or ("problem" and "solving")
#     ) and ("resources" or "resource") in keywords:
#         return f"Data structures and algorithms are the building blocks of computer science. For specific resources, refer here - {https://discord.com/channels/781467057807032323/1038729955623845888}"
#     # AI/ML
#     elif ("ai" or "artificial intelligence" or "ml" or "machine learning") and (
#         "resources" or "resource"
#     ) in keywords:
#         return f"Artificial intelligence is the simulation of human intelligence processes by machines. For specific resources, refer here - {https://discord.com/channels/781467057807032323/1230506240854200362}"
#     # Blockchain
#     elif ("blockchain" or "web3") and ("resources" or "resource") in keywords:
#         return f"Blockchain is a system in which a record of transactions made in bitcoin or another cryptocurrency are maintained across several computers that are linked in a peer-to-peer network. For specific resources, refer here - {https://discord.com/channels/781467057807032323/1247586354075009116}"
#     # Open Source
#     elif "open source" and ("resources" or "resource") in keywords:
#         return f"Open-source software is a type of computer software in which source code is released under a license in which the copyright holder grants users the rights to use, study, change, and distribute the software. For specific resources, refer here - {https://discord.com/channels/781467057807032323/1035874500639719495}"
#     # General Resources
#     elif "general" and ("resources" or "resource") in keywords:
#         return f"General resources are resources that are not specific to any domain. For specific resources, refer here - {https://discord.com/channels/781467057807032323/1213918549425397810}"
#     # UI/UX
#     elif ("ui" or "ux" or "ui/ux") and ("resources" or "resource") in keywords:
#         return f"UI/UX design is the process design teams use to create products that provide meaningful and relevant experiences to users. For specific resources, refer here - {https://discord.com/channels/781467057807032323/1230553508814524446}"
#     # DevOps
#     elif ("devops" or "ci/cd" or ("dev" and "ops")) and (
#         "resources" or "resource"
#     ) in keywords:
#         return f"DevOps is a set of practices that combines software development and IT operations. For specific resources, refer here - {https://discord.com/channels/781467057807032323/1045021472860688454}"
#     # System (Windows) Programming
#     elif ("system" and "programming" and "windows") and (
#         "resources" or "resource"
#     ) in keywords:
#         return f"System programming is the activity of programming computer system software. For specific resources, refer here - {https://discord.com/channels/781467057807032323/1110099353256865842}"
#     # Embedded Systems
#     elif ("embedded" and "systems") and ("resources" or "resource") in keywords:
#         return f"An embedded system is a computer system—a combination of a computer processor, computer memory, and input/output peripheral devices—that has a dedicated function within a larger mechanical or electrical system. For specific resources, refer here - {https://discord.com/channels/781467057807032323/1108716008279117974}"
#     # Cybersecurity
#     elif ("cybersecurity" or "security" or ("cyber" and "security")) and (
#         "resources" or "resource"
#     ) in keywords:
#         return f"Cybersecurity is the practice of protecting systems, networks, and programs from digital attacks. For specific resources, refer here - {https://discord.com/channels/781467057807032323/1035874742248419358}"
#     # Game Development
#     elif ("game" and ("development" or "dev")) and (
#         "resources" or "resource"
#     ) in keywords:
#         return f"Game development is the process of creating video games. For specific resources, refer here - {https://discord.com/channels/781467057807032323/1035874649046790216}"
#     # CP
#     elif ("cp" or ("competitive" and "programming")) and (
#         "resources" or "resource"
#     ) in keywords:
#         return f"Competitive programming is a mind sport usually held over the Internet or a local network, involving participants trying to program according to provided specifications. For specific resources, refer here - {https://discord.com/channels/781467057807032323/1035874325921804388}"
#     else:
#         # return choice(['Hey sorry, what did you say?!',
#         #                'I did not understand that bbg!',
#         #                'I am not sure what you mean bbg!',
#         #                "Can you say that again?"])
#         pass

from random import choice, randint

# Dictionary to store resource links and corresponding keywords
resources = {
    (
        "cpp",
        "c++",
    ): "https://discord.com/channels/781467057807032323/1035869217074978886",
    ("python",): "https://discord.com/channels/781467057807032323/1035869711004618834",
    ("java",): "https://discord.com/channels/781467057807032323/1045022001762418779",
    (
        "javascript",
        "js",
    ): "https://discord.com/channels/781467057807032323/1045027084717797436",
    (
        "golang",
        "go",
    ): "https://discord.com/channels/781467057807032323/1192175876213833799",
    ("rust",): "https://discord.com/channels/781467057807032323/1038338641421938738",
    (
        "typescript",
        "ts",
    ): "https://discord.com/channels/781467057807032323/1247558205165535383",
    (
        "clean code",
    ): "https://discord.com/channels/781467057807032323/1185484608205238332",
    (
        "cs basics",
    ): "https://discord.com/channels/781467057807032323/1251496416203903027",
    (
        "system programming",
        "linux",
    ): "https://discord.com/channels/781467057807032323/1108712976971730956",
    (
        "web development",
        "web dev",
        "html",
        "css",
    ): "https://discord.com/channels/781467057807032323/1035874106605842553",
    (
        "app development",
        "app dev",
        "android",
        "ios",
        "app",
    ): "https://discord.com/channels/781467057807032323/1035874202886086657",
    ("flutter",): "https://discord.com/channels/781467057807032323/1176525373148774501",
    (
        "dsa",
        "data structures",
        "algorithms",
        "problem solving",
        "ps",
    ): "https://discord.com/channels/781467057807032323/1038729955623845888",
    (
        "ai",
        "artificial intelligence",
        "ml",
        "machine learning",
    ): "https://discord.com/channels/781467057807032323/1230506240854200362",
    (
        "blockchain",
        "web3",
    ): "https://discord.com/channels/781467057807032323/1247586354075009116",
    (
        "open source",
    ): "https://discord.com/channels/781467057807032323/1035874500639719495",
    (
        "general resources",
    ): "https://discord.com/channels/781467057807032323/1213918549425397810",
    (
        "ui/ux",
        "ui",
        "ux",
    ): "https://discord.com/channels/781467057807032323/1230553508814524446",
    (
        "devops",
        "ci/cd",
        "dev ops",
    ): "https://discord.com/channels/781467057807032323/1045021472860688454",
    (
        "system programming",
        "windows",
    ): "https://discord.com/channels/781467057807032323/1110099353256865842",
    (
        "embedded systems",
    ): "https://discord.com/channels/781467057807032323/1108716008279117974",
    (
        "cybersecurity",
        "cyber security",
        "security",
    ): "https://discord.com/channels/781467057807032323/1035874742248419358",
    (
        "game development",
        "game dev",
    ): "https://discord.com/channels/781467057807032323/1035874649046790216",
    (
        "cp",
        "competitive programming",
    ): "https://discord.com/channels/781467057807032323/1035874325921804388",
}


def get_resource_link(keywords: list[str], resources: dict) -> str:
    for resource_keywords, link in resources.items():
        if any(keyword in keywords for keyword in resource_keywords):
            return link
    return None


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    keywords: list[str] = lowered.strip().split()

    # Basic responses
    if lowered == "":
        return "Well, I can't respond to nothing, can I?"
    elif lowered == "hi":
        return "Hello bbg!"
    elif lowered == "bye":
        return "Goodbye bbg!"
    elif lowered == "roll dice":
        return f"You rolled a {randint(1, 6)}!"
    elif lowered == "flip a coin":
        return choice(["Heads!", "Tails!"])
    elif lowered == "how are you":
        return "I'm doing fine bbg, tell me about yourself!"

    # printing the link to the specific resources
    resource_link = get_resource_link(keywords, resources)
    if resource_link:
        return f"For specific resources, refer here - {resource_link}"

    # Default responses
    return choice(
        [
            "Hey sorry, what did you say?!",
            "I did not understand that bbg!",
            "I am not sure what you mean bbg!",
            "Can you say that again?",
        ]
    )
