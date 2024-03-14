from datetime import datetime


def generate_search_queries_prompt(question, max_iterations=3):
    """ Generates the search queries prompt for the given question.
    Args: question (str): The question to generate the search queries prompt for
    Returns: str: The search queries prompt for the given question
    """

    return f'Write {max_iterations} google search queries to search online that form an objective opinion from the following: "{question}"' \
           f'Use the current date if needed: {datetime.now().strftime("%B %d, %Y")}.\n' \
           f'You must respond with a list of strings in the following format: ["query 1", "query 2", "query 3"].'

def generate_readme_report_prompt(question, context, report_format="apa", total_words=1000):
# def generate_readme_report_prompt(project_name, research_summary):
    """
    Generates the README.md report prompt for the given project and research summary.

    Args:
        project_name (str): The name of the project to generate the report prompt for.
        research_summary (str): The research summary to generate the report prompt for.

    Returns:
        str: The README.md report prompt for the given project and research summary.
    """


    return f'"""{context}""" Based on the provided information, research and implement a comprehensive README.md'\
           f' guide for the "{question}" question. The guide should provide clear instructions on how to set up'\
           f' the project, including installation steps, dependencies, and configuration details. Include information'\
           f' on project structure, file organization, and usage examples. Provide explanations of key concepts,'\
           f' features, and functionality. Consider best practices for documentation and readability. Ensure that the'\
           f' guide is well-structured, informative, and follows appropriate formatting (Markdown syntax). Write all'\
           f' source URLs at the end of the guide in APA format. The guide should have a minimum length of 1,200 words'\
           f' and with Markdown syntax and APA format.'

def generate_medical_research_report_prompt(question, context, report_format="apa", total_words=1500):
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

def generate_software_architecture_report_prompt(question, context, report_format="apa", total_words=2000):
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

def generate_market_analysis_report_prompt(question, context, report_format="apa", total_words=1200):
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
        'research_report': generate_report_prompt,
        'readme_report': generate_readme_report_prompt,
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

