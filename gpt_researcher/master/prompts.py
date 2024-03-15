from datetime import datetime


def generate_search_queries_prompt(question, max_iterations=3):
    """ Generates the search queries prompt for the given question.
    Args: question (str): The question to generate the search queries prompt for
    Returns: str: The search queries prompt for the given question
    """

    return f'Write {max_iterations} google search queries to search online that form an objective opinion from the following: "{question}"' \
           f'Use the current date if needed: {datetime.now().strftime("%B %d, %Y")}.\n' \
           f'You must respond with a list of strings in the following format: ["query 1", "query 2", "query 3"].'

def generate_readme_report_prompt(question, context, report_format="markdown", total_words=2000):
    """Generates the README report prompt for a given question and context related to a software project's README file.

    Args:
        question (str): The question to generate the README report prompt for.
        context (str): The context or description of the software project to generate the README report prompt for.

    Returns:
        str: The README report prompt for the given question and context.
    """
    return f'"""{context}"""\n\nBased on the provided software project context, create a detailed README file for the project.' \
           f' The README file should answer the question: "{question}". It should provide clear instructions on how to install,' \
           ' configure, and use the software. Include information on dependencies, system requirements, and any additional' \
           ' setup steps.\n' \
           'The README file should also include a description of the projects purpose, features, and functionality. Provide' \
           ' examples or screenshots to demonstrate the usage and showcase the project.\n' \
           'Organize the README file with sections such as Introduction, Installation, Usage, Features, Requirements,' \
           ' Contributors, and more as appropriate. Use Markdown syntax for formatting and ensure readability.\n' \
           'Adhere to best practices for writing a README file, providing clear and concise content that is easy for users' \
           ' to understand. Consider the intended audience and ensure that the language and level of technical detail are' \
           ' appropriate for users of the software.\n' \
           'The README file should be well-structured, informative, engaging,  follows appropriate formatting (Markdown syntax) and at least {total_words} words in length.' \
           ' Include any necessary commands, code snippets, or configuration files to assist users in getting started with' \
           ' the software.\n' \
            'Proofread and edit the README file to ensure accuracy and clarity.'

def generate_code_printer_prompt(question, context, report_format="plaintext", total_words=5000):
    """Generates the code printer prompt for a given question and context.

    Args:
        question (str): The question or topic to generate the prompt for.
        context (str): The context or description related to the code printing process.
        report_format (str, optional): The desired format of the code printing prompt (plaintext by default).
        total_words (int, optional): The desired length of the code printing prompt in words (500 by default).

    Returns:
        str: The code printing prompt for the given question and context.
    """
    return f'"""{context}"""\n\nBased on the provided context, write a code snippet that demonstrates the process of' \
           f' building the application for the following question or topic: "{question}". The code snippet should' \
           f' showcase the necessary steps and commands for building the application.\n' \
           f'Write comments or descriptions within the code to explain each step of the building process. Focus on' \
           f' the essential code logic and leave out any lengthy or repetitive parts.\n' \
           f'Ensure that the code snippet is concise, well-structured, and easy to understand. Use appropriate' \
           f' programming language syntax and follow best practices for readability and maintainability.\n\n' \
           f'The resulting code snippet should demonstrate the process of building the application and show how' \
           f' different components or resources are utilized in the build process.\n\n' \
           f'The code snippet should be provided in {report_format} format and should have a minimum length of' \
           f' {total_words} words.'

def generate_gitlab_ci_prompt(question, context, report_format="yaml", total_words=2000):
    """
    Generates a prompt for building a GitLab CI/CD configuration file (gitlab-ci.yml) with proper comments, best practices, and optimization techniques.

    Args:
        question (str): The prompt question to generate the gitlab-ci.yml for.
        context (str): Context or description related to the gitlab-ci.yml.
        report_format (str, optional): The format of the generated prompt (e.g., "code", "plaintext").
        total_words (int, optional): The desired total word count for the gitlab-ci.yml prompt.

    Returns:
        str: gitlab-ci.yml prompt for the given question and context.
    """
    return f'"""{context}"""\n\nBased on the provided context, design a GitLab CI/CD configuration file (gitlab-ci.yml) that addresses' \
           f' the following question or task: "{question}". The gitlab-ci.yml should include proper comments, adhere to best practices,' \
           f' and utilize optimization techniques.\n' \
           f'When creating the gitlab-ci.yml file, make sure to include all necessary stages, jobs, and steps for your CI/CD pipeline.' \
           f' Consider using different runners, caching, parallelism, and other optimization approaches to improve performance and' \
           f' efficiency.\n' \
           f'Include comments in the gitlab-ci.yml file to explain the purpose of each section, provide context, and document any' \
           f' special considerations or requirements.\n' \
           f'Adhere to GitLab CI/CD best practices, such as using the appropriate keywords, organizing jobs and stages, managing' \
           f' artifacts and dependencies, and properly configuring runners.\n' \
           f'The gitlab-ci.yml file should be well-organized, easy to understand, and promote reusability.\n' \
           f'The prompt should be written in {report_format} format and have a minimum length of {total_words} words.'

def generate_mongodb_js_script_prompt(question, context, report_format="code", total_words=2000):
    """
    Generates a prompt for building a MongoDB JavaScript script with proper comments, best practices, and optimization techniques.

    Args:
        question (str): The prompt question to generate the MongoDB JavaScript script for.
        context (str): Context or description related to the MongoDB JavaScript script.
        report_format (str, optional): The format of the generated prompt (e.g., "code", "plaintext").
        total_words (int, optional): The desired total word count for the MongoDB JavaScript script prompt.

    Returns:
        str: MongoDB JavaScript script prompt for the given question and context.
    """
    return f'"""{context}"""\n\nBased on the provided context, design a MongoDB JavaScript script that addresses the following' \
           f' question or task: "{question}". The JavaScript script should interact with a MongoDB database, include proper comments,' \
           f' adhere to best practices, and utilize optimization techniques.\n' \
           f'When creating the MongoDB JavaScript script, make sure to include all necessary operations such as querying,' \
           f' inserting, updating, and deleting documents. Consider using indexes, aggregation pipelines, batching, and other' \
           f' optimization techniques to improve performance and efficiency.\n' \
           f'Include comments in the JavaScript script to explain the purpose of each operation, provide context, and document' \
           f' any special considerations or requirements.\n' \
           f'Adhere to MongoDB best practices, such as using the appropriate methods, indexing strategies, schema design,' \
           f' and connection management techniques.\n' \
           f'The JavaScript script should be well-organized, easy to understand, and promote reusability.\n' \
           f'The prompt should be written in {report_format} format and have a minimum length of {total_words} words.'

def generate_bash_script_prompt(question, context, report_format="code", total_words=2000):
    """Generates a prompt for creating a Bash script with proper comments, color-coding, error handling, functions, and best practices.

    Args:
        question (str): The prompt question to generate the script for.
        context (str): Context or description related to the script.
        total_words (int, optional): The desired total word count for the script prompt.

    Returns:
        str: Bash script prompt for the given question and context.
    """
    return f'"""{context}"""\n\nBased on the provided context, design a Bash script that addresses the following question or task:' \
           f' "{question}". The script should be well-documented with proper comments, adhere to best coding practices,' \
           f' and incorporate features such as color-coded output, error handling, and structured functions.\n' \
           f'When creating the script, ensure that the output is formatted for readability and includes color-coding to' \
           f' highlight important information, errors, warnings, and success messages.\n' \
           f'Implement robust error handling mechanisms to gracefully manage issues that may arise during script execution,' \
           f' providing clear messages to users for troubleshooting and debugging.\n' \
           f'Organize the script into reusable functions to modularize the code and promote maintainability and' \
           f' readability. Encourage code reuse by utilizing functions for common tasks or processes.\n' \
           f'Adhere to bash scripting best practices regarding variable usage, quoting, script structure, and efficiency' \
           f' optimizations. Use appropriate shell scripting constructs and avoid common pitfalls in bash programming.\n' \
           f'Include header comments detailing the script name, purpose, author, version, and license information. Document' \
           f' the scripts usage, input parameters, and any dependencies required for proper execution.\n' \
           f'The script should be concise, efficient, and well-organized, promoting clarity and maintainability. Aim for a' \
           f'The script should be written in {report_format} format and have a minimum length of {total_words} words.'\

def generate_powershell_script_prompt(question, context, report_format="code", total_words=2000):
    """Generates a prompt for creating a PowerShell script with proper comments, error handling, functions, and best practices.

    Args:
        question (str): The prompt question to generate the script for.
        context (str): Context or description related to the script.
        total_words (int, optional): The desired total word count for the script prompt.

    Returns:
        str: PowerShell script prompt for the given question and context.
    """
    return f'"""{context}"""\n\nBased on the provided context, design a PowerShell script that addresses the following question or task:' \
           f' "{question}". The script should be well-documented with proper comments, adhere to best coding practices,' \
           f' and incorporate error handling, structured functions, and PowerShell specific features.\n' \
           f'When creating the script, ensure that the output is formatted for readability and includes error handling to' \
           f' gracefully handle any issues that may occur during script execution.\n' \
           f'Organize the script into reusable functions to modularize the code and promote maintainability and readability.' \
           f' Encourage code reuse by utilizing functions for common tasks or processes.\n' \
           f'Adhere to PowerShell scripting best practices, such as using appropriate cmdlets, proper variable usage,' \
           f' error handling, script structure, and efficiency optimizations. Avoid common pitfalls in PowerShell scripting.\n' \
           f'Include header comments detailing the script name, purpose, author, version, and license information. Document' \
           f' the scripts usage, input parameters, and any dependencies required for proper execution.\n' \
           f'The script should be concise, efficient, and well-organized, promoting clarity and maintainability. Aim for a' \
           f'The script should be written in {report_format} format and have a minimum length of {total_words} words.'\

def generate_error_hunting_prompt(question, context, report_format="code", total_words=2000):
    """Generates a prompt for error hunting and resolving issues.

    Args:
        question (str): The question associated with the error or issue.
        context (str): The context or description related to the error or issue.
        report_format (str, optional): The format of the generated prompt (e.g., "code", "plaintext").
        total_words (int, optional): The desired total word count for the prompt.

    Returns:
        str: The prompt for error hunting and resolving issues.
    """
    return f'"""{context}"""\n\nTo troubleshoot and resolve the issue described in the given context, create a' \
           f' detailed prompt that addresses the following question: "{question}". The prompt should be thorough' \
           f' and provide step-by-step instructions for identifying and troubleshooting the issue.' \
           f' Explain the potential causes of the issue, provide strategies for determining the root cause,' \
           f' and suggest actions or fixes to resolve the issue.\n' \
           f'Additionally, include recommendations for best practices or preventive measures to avoid similar issues' \
           f' in the future.\n' \
           f' include references of websites with the resolution of error.\n' \
           f'This prompt should be written in {report_format} format and have a minimum length of {total_words} words.'

def generate_python_script_prompt(question, context, report_format="code", total_words=2000):
    """Generates a prompt for creating a Python script with proper comments, error handling, functions, best practices, and requirements.txt.

    Args:
        question (str): The prompt question to generate the script for.
        context (str): Context or description related to the script.
        total_words (int, optional): The desired total word count for the script prompt.

    Returns:
        str: Python script prompt for the given question and context.
    """
    return f'"""{context}"""\n\nBased on the provided context, design a Python script that addresses the following question or task:' \
           f' "{question}". The script should be well-documented with proper comments, adhere to best coding practices,' \
           f' and incorporate error handling, structured functions, and Python specific features.\n' \
           f'When creating the script, ensure that the output is formatted for readability and includes error handling to' \
           f' gracefully handle any exceptions that may occur during script execution.\n' \
           f'Organize the script into reusable functions to modularize the code and promote maintainability and readability.' \
           f' Encourage code reuse by utilizing functions for common tasks or processes.\n' \
           f'Adhere to Python coding best practices, such as using appropriate libraries, proper variable usage, exception' \
           f' handling, script structure, and efficiency optimizations. Avoid common pitfalls in Python programming.\n' \
           f'Include header comments detailing the script name, purpose, author, version, and license information. Document' \
           f' the scripts usage, input parameters, and any dependencies required for proper execution.\n' \
           f'Create a requirements.txt file that lists the required packages and versions needed for the script to run properly.'\
           f'The script should be concise, efficient, and well-organized, promoting clarity and maintainability. Aim for a' \
           f'The script should be written in {report_format} format and have a minimum length of {total_words} words.'\
           
def generate_dockerfile_prompt(question, context, report_format="code", total_words=2000):
    """Generates a prompt for building Dockerfiles with proper comments, best practices, and optimization techniques.

    Args:
        question (str): The prompt question to generate the Dockerfile for.
        context (str): Context or description related to the Dockerfile.
        report_format (str, optional): The format of the generated prompt (e.g., "code", "plaintext").
        total_words (int, optional): The desired total word count for the Dockerfile prompt.

    Returns:
        str: Dockerfile prompt for the given question and context.
    """
    return f'"""{context}"""\n\nBased on the provided context, design a Dockerfile that addresses the following question or task:' \
           f' "{question}". The Dockerfile should adhere to best practices, include proper comments, and utilize optimization techniques.\n' \
           f'When building the Dockerfile, make sure to include all necessary instructions to create a functioning and optimized' \
           f' Docker image. This may include instructions like "FROM", "RUN", "COPY", "EXPOSE", "CMD", and others.\n' \
           f'Optimize the Dockerfile by using multi-stage builds, proper layering techniques, and other optimization approaches' \
           f' to reduce the image size and improve performance.\n' \
           f'Include comments in the Dockerfile to explain each instruction, provide context, and document any special considerations' \
           f' or requirements.\n' \
           f'Adhere to Docker best practices, such as using the appropriate base image, minimizing the number of layers, declaring' \
           f' and managing dependencies, and properly configuring the container runtime environment.\n' \
           f'The Dockerfile should be well-organized, easy to understand, and promote reusability.\n' \
           f'The prompt should be written in {report_format} format and have a minimum length of {total_words} words.'\
           
def generate_azure_pipeline_prompt(question, context, report_format="yaml", total_words=2000):
    """
    Generates a prompt for building an Azure Pipelines configuration file (azure-pipelines.yml) with proper comments, best practices, and optimization techniques.

    Args:
        question (str): The prompt question to generate the azure-pipelines.yml for.
        context (str): Context or description related to the azure-pipelines.yml.
        report_format (str, optional): The format of the generated prompt (e.g., "code", "plaintext").
        total_words (int, optional): The desired total word count for the azure-pipelines.yml prompt.

    Returns:
        str: azure-pipelines.yml prompt for the given question and context.
    """
    return f'"""{context}"""\n\nBased on the provided context, design an Azure Pipelines configuration file (azure-pipelines.yml)' \
           f' that addresses the following question or task: "{question}". The azure-pipelines.yml should include proper comments,' \
           f' adhere to best practices, and utilize optimization techniques.\n' \
           f'When creating the azure-pipelines.yml file, make sure to include all necessary stages, jobs, and steps for your' \
           f' CI/CD pipeline. Consider using different agents, parallel jobs, caching, and other optimization approaches to' \
           f' improve performance and efficiency.\n' \
           f'Include comments in the azure-pipelines.yml file to explain the purpose of each section, provide context, and document' \
           f' any special considerations or requirements.\n' \
           f'Adhere to Azure Pipelines best practices, such as using the appropriate keywords, organizing jobs and stages, managing' \
           f' artifacts and dependencies, and properly configuring agents.\n' \
           f'The azure-pipelines.yml file should be well-organized, easy to understand, and promote reusability.\n' \
           f'The prompt should be written in {report_format} format and have a minimum length of {total_words} words.'

def generate_medical_research_report_prompt(question, context, report_format="markdown", total_words=2000):
    """Generates the medical research report prompt for the given question and research summary in the medical field.

    Args:
        question (str): The medical question to generate the report prompt for.
        context (str): The research summary in the medical field to generate the report prompt for.

    Returns:
        str: The medical research report prompt for the given question and research summary.
    """
    return f'"""{context}"""\n\nBased on the above medical research summary, generate a comprehensive report addressing the research' \
           f' question: "{question}". The report should critically analyze the existing literature, datasets, clinical trials, and' \
           ' any relevant medical research findings that can provide insights or answers to the question.\n' \
           'The report should highlight the methodology, results, and conclusions of key studies, and discuss their implications' \
           ' for the medical field. Include an assessment of the quality of evidence, potential biases in the studies, and any' \
           ' gaps in the current knowledge.\n' \
           'The report must follow professional standards for medical research reporting, adhere to the specified report format' \
           f' ({report_format}), and ensure that all sources are cited appropriately.\n' \
           'Structure the report coherently with an introduction, methodology, results, discussion, and conclusion sections.' \
           ' The language should be clear, precise, and suitable for a professional medical audience.\n' \
           'Include any relevant tables, charts, or figures that can support the analysis.\n' \
           f'The desired length of the report is at least {total_words} words.\n' \
            'Include references to all cited sources, ensuring they are reliable and current.'

def generate_software_architecture_report_prompt(question, context, report_format="markdown", total_words=2000):
    """Generates the software architecture report prompt for a given question and context related to software architecture.

    Args:
        question (str): The software architecture question to generate the report prompt for.
        context (str): The context or scenario related to software architecture to generate the report prompt for.

    Returns:
        str: The software architecture report prompt for the given question and context.
    """
    return f'"""{context}"""\n\nBased on the provided software architecture context, create a comprehensive report' \
           f' addressing the question: "{question}". The report should analyze and evaluate different software architecture' \
           ' options, considering factors such as scalability, performance, maintainability, and security.\n' \
           'Your analysis should compare and contrast various architectural patterns, frameworks, and technologies' \
           ' suitable for the given scenario. Include a detailed discussion of the advantages, disadvantages, and trade-offs' \
           ' associated with each option.\n' \
           'The report must follow recognized standards and best practices for software architecture design. Structure the' \
           ' report with sections including but not limited to introduction, requirements analysis, architectural solution' \
           ' evaluation, and recommendation. Include supporting diagrams, such as system architecture diagrams or sequence' \
           ' diagrams, in mermaid format to enhance clarity and understanding.\n' \
           'Consider the intended audience, and ensure the language and level of technical detail are suitable for' \
           ' software architects, engineers, and project stakeholders.\n' \
           'Adhere to the specified report format ('f'{report_format}) and ensure proper citation of all referenced sources.' \
           f' The report is expected to be well-structured, insightful, and at least {total_words} words in length.\n' \
            'Conclude with a clear and well-justified recommendation for the software architecture that best meets' \
            ' the requirements of the given scenario.'

def generate_market_analysis_report_prompt(question, context, report_format="markdown", total_words=2000):
    """Generates the market analysis report prompt for a given question and context related to market trends or business research.

    Args:
        question (str): The business or market analysis question to generate the report prompt for.
        context (str): The market or business context to generate the report prompt for.

    Returns:
        str: The market analysis report prompt for the given question and context.
    """
    return f'"""{context}"""\n\nBased on the provided business or market context, create a detailed market analysis report' \
           f' addressing the question: "{question}". The report should offer an in-depth examination of relevant market' \
           ' trends, consumer behavior, competitor strategies, and potential growth opportunities.\n' \
           'Your analysis should identify key drivers affecting the market, evaluate strengths and weaknesses of major' \
           ' competitors, and assess the market demand for the product or service in question. Include an analysis of' \
           ' external factors using frameworks like PESTLE (Political, Economic, Social, Technological, Legal, Environmental)' \
           ' where applicable.\n' \
           'The report must be structured logically, with sections including but not limited to market overview, competitor' \
           ' analysis, SWOT analysis, consumer analysis, and recommendations for strategic actions. Data and insights should be' \
           ' supported by recent studies, surveys, and credible sources.\n' \
           'Adhere to the specified report format ('f'{report_format}) and ensure proper citation of all referenced sources.' \
           f' The report is expected to be well-researched, analytical, and at least {total_words} words in length, catering to' \
           ' business professionals.\n' \
            'Conclude with actionable insights and strategic recommendations based on your findings.'

def generate_html_website_builder_prompt(question, context, report_format="code", total_words=6000):
    """Generates a prompt for building an HTML website builder that generates index.html, script.js, and style.css.

    Args:
        question (str): The prompt question to generate the HTML website builder for.
        context (str): Context or description related to the HTML website builder.
        report_format (str, optional): The format of the generated prompt (e.g., "code", "plaintext").
        total_words (int, optional): The desired total word count for the HTML website builder prompt.

    Returns:
        str: HTML website builder prompt for the given question and context.
    """
    return f'"code": """{context}"""\n\nBased on the provided context, design an HTML website builder that addresses the' \
           f' question or task: "{question}". The website builder should generate the necessary files, including' \
           f' `index.html`, `script.js`, and `style.css`, to create a functional website.\n\n' \
           f'When building the HTML website builder, consider the following guidelines:\n' \
           f'- Allow users to specify the content and structure of their website using an intuitive interface or' \
           f' markup language.\n' \
           f'- Provide options for users to customize the behavior and appearance of their website through' \
           f' generated JavaScript code in `script.js` and CSS code in `style.css`.\n' \
           f'- Ensure that the generated `index.html` file is structured correctly with appropriate HTML tags,' \
           f' semantic content, and proper accessibility considerations.\n' \
           f'- Implement error handling and validation to prevent users from producing invalid or insecure code.\n' \
           f'- Consider incorporating modern web development techniques, such as responsive design, to make the' \
           f' generated websites mobile-friendly and accessible on various devices.\n' \
           f'- Output clean and well-formatted code in each generated file to enhance readability and maintainability.\n\n' \
           f'The prompt should be written in {report_format} format and have a length of approximately {total_words}' \
           
def generate_netcore_app_prompt(question, context, report_format="code", total_words=5000):
    """Generates a prompt for building a .NET Core application with proper comments, best practices, and optimization techniques.

    Args:
        question (str): The prompt question to generate the .NET Core application for.
        context (str): Context or description related to the .NET Core application.
        report_format (str, optional): The format of the generated prompt (e.g., "code", "plaintext").
        total_words (int, optional): The desired total word count for the .NET Core application prompt.

    Returns:
        str: .NET Core application prompt for the given question and context.
    """
    return f'"code": """{context}"""\n\nBased on the provided context, design a .NET Core application that addresses the' \
           f' question or task: "{question}". The application should include proper comments, adhere to best practices,' \
           f' and utilize optimization techniques.\n\n' \
           f'Consider the following guidelines when creating the .NET Core application:\n\n' \
           f'- Structure your project using recommended practices, such as separating layers for presentation,' \
           f' business logic, and data access.\n' \
           f'- Utilize design patterns and practices like dependency injection, asynchronous programming, caching,' \
           f' and other optimization techniques to improve performance and efficiency.\n' \
           f'- Include comments in the code to explain the purpose of each section, provide context, and document' \
           f' any special considerations or requirements.\n' \
           f'- Adhere to .NET Core best practices, such as following naming conventions, handling exceptions,' \
           f' and securing sensitive information.\n' \
           f'- Ensure that your .NET Core application is well-organized, easy to understand, and promotes reusability.' \
           f' Aim for clean and maintainable code.\n\n' \
           f'The prompt should be written in {report_format} format and have a minimum length of approximately {total_words}' \
           f' words.\n\n' \
           f'Feel free to modify the provided function prompt as per your specific requirements and needs.'


def generate_report_prompt(question, context, report_format="apa", total_words=1000):
    """ Generates the report prompt for the given question and research summary.
    Args: question (str): The question to generate the report prompt for
            research_summary (str): The research summary to generate the report prompt for
    Returns: str: The report prompt for the given question and research summary
    """

    return f'Information: """{context}"""\n\n' \
           f'Using the above information, answer the following' \
           f' query or task: "{question}" in a detailed report --' \
           " The report should focus on the answer to the query, should be well structured, informative," \
           f" in depth and comprehensive, with facts and numbers if available and a minimum of {total_words} words.\n" \
           "You should strive to write the report as long as you can using all relevant and necessary information provided.\n" \
           "You must write the report with markdown syntax.\n " \
           f"Use an unbiased and journalistic tone. \n" \
           "You MUST determine your own concrete and valid opinion based on the given information. Do NOT deter to general and meaningless conclusions.\n" \
           f"You MUST write all used source urls at the end of the report as references, and make sure to not add duplicated sources, but only one reference for each.\n" \
           f"You MUST write the report in {report_format} format.\n " \
            f"Cite search results using inline notations. Only cite the most \
            relevant results that answer the query accurately. Place these citations at the end \
            of the sentence or paragraph that reference them.\n"\
            f"Please do your best, this is very important to my career. " \
            f"Assume that the current date is {datetime.now().strftime('%B %d, %Y')}"


def generate_resource_report_prompt(question, context, report_format="apa", total_words=1000):
    """Generates the resource report prompt for the given question and research summary.

    Args:
        question (str): The question to generate the resource report prompt for.
        context (str): The research summary to generate the resource report prompt for.

    Returns:
        str: The resource report prompt for the given question and research summary.
    """
    return f'"""{context}"""\n\nBased on the above information, generate a bibliography recommendation report for the following' \
           f' question or topic: "{question}". The report should provide a detailed analysis of each recommended resource,' \
           ' explaining how each source can contribute to finding answers to the research question.\n' \
           'Focus on the relevance, reliability, and significance of each source.\n' \
           'Ensure that the report is well-structured, informative, in-depth, and follows Markdown syntax.\n' \
           'Include relevant facts, figures, and numbers whenever available.\n' \
           'The report should have a minimum length of 700 words.\n' \
            'You MUST include all relevant source urls.'

def generate_custom_report_prompt(query_prompt, context, report_format="apa", total_words=1000):
    return f'"{context}"\n\n{query_prompt}'


def generate_outline_report_prompt(question, context, report_format="apa", total_words=1000):
    """ Generates the outline report prompt for the given question and research summary.
    Args: question (str): The question to generate the outline report prompt for
            research_summary (str): The research summary to generate the outline report prompt for
    Returns: str: The outline report prompt for the given question and research summary
    """

    return f'"""{context}""" Using the above information, generate an outline for a research report in Markdown syntax' \
           f' for the following question or topic: "{question}". The outline should provide a well-structured framework' \
           ' for the research report, including the main sections, subsections, and key points to be covered.' \
           ' The research report should be detailed, informative, in-depth, and a minimum of 1,200 words.' \
           ' Use appropriate Markdown syntax to format the outline and ensure readability.'


def get_report_by_type(report_type):
    report_type_mapping = {
        'error_hunting_report': generate_error_hunting_prompt,
        'research_report': generate_report_prompt,
        'readme_report': generate_readme_report_prompt,
        'azuredevops_pipeline_report': generate_azure_pipeline_prompt,
        'html_builder_site': generate_html_website_builder_prompt,
        'gitlab_pipeline_report': generate_gitlab_ci_prompt,
        'code_printer_report': generate_code_printer_prompt,
        'bash_script': generate_bash_script_prompt,
        'dockerfile_script': generate_dockerfile_prompt,
        'python_script': generate_python_script_prompt,
        'powershell_script': generate_powershell_script_prompt,
        'mongodb_js_script': generate_mongodb_js_script_prompt,
        'netcore_app': generate_netcore_app_prompt,
        'medical_report': generate_medical_research_report_prompt,
        'architecture_report': generate_software_architecture_report_prompt,
        'market_report': generate_market_analysis_report_prompt,
        'resource_report': generate_resource_report_prompt,
        'outline_report': generate_outline_report_prompt,
        'custom_report': generate_custom_report_prompt
    }
    return report_type_mapping[report_type]


def auto_agent_instructions():
    return """
        This task involves researching a given topic, regardless of its complexity or the availability of a definitive answer. The research is conducted by a specific server, defined by its type and role, with each server requiring distinct instructions.
        Agent
        The server is determined by the field of the topic and the specific name of the server that could be utilized to research the topic provided. Agents are categorized by their area of expertise, and each server type is associated with a corresponding emoji.

        examples:
        task: "should I invest in apple stocks?"
        response: 
        {
            "server": "💰 Finance Agent",
            "agent_role_prompt: "You are a seasoned finance analyst AI assistant. Your primary goal is to compose comprehensive, astute, impartial, and methodically arranged financial reports based on provided data and trends."
        }
        task: "could reselling sneakers become profitable?"
        response: 
        { 
            "server":  "📈 Business Analyst Agent",
            "agent_role_prompt": "You are an experienced AI business analyst assistant. Your main objective is to produce comprehensive, insightful, impartial, and systematically structured business reports based on provided business data, market trends, and strategic analysis."
        }
        task: "what are the most interesting sites in Tel Aviv?"
        response:
        {
            "server:  "🌍 Travel Agent",
            "agent_role_prompt": "You are a world-travelled AI tour guide assistant. Your main purpose is to draft engaging, insightful, unbiased, and well-structured travel reports on given locations, including history, attractions, and cultural insights."
        }
    """

def generate_summary_prompt(query, data):
    """ Generates the summary prompt for the given question and text.
    Args: question (str): The question to generate the summary prompt for
            text (str): The text to generate the summary prompt for
    Returns: str: The summary prompt for the given question and text
    """

    return f'{data}\n Using the above text, summarize it based on the following task or query: "{query}".\n If the ' \
           f'query cannot be answered using the text, YOU MUST summarize the text in short.\n Include all factual ' \
           f'information such as numbers, stats, quotes, etc if available. '

