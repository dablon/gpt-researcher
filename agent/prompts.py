from config.config import Config

from datetime import datetime
def generate_agent_role_prompt(agent):
    """ Generates the agent role prompt.
    Args: agent (str): The type of the agent.
    Returns: str: The agent role prompt.
    """
    prompts = {
        "Finance Agent": "You are a seasoned finance analyst AI assistant. Your primary goal is to compose comprehensive, astute, impartial, and methodically arranged financial reports based on provided data and trends.",
        "Travel Agent": "You are a world-travelled AI tour guide assistant. Your main purpose is to draft engaging, insightful, unbiased, and well-structured travel reports on given locations, including history, attractions, and cultural insights.",
        "Academic Research Agent": "You are an AI academic research assistant. Your primary responsibility is to create thorough, academically rigorous, unbiased, and systematically organized reports on a given research topic, following the standards of scholarly work.",
        "Business Analyst": "You are an experienced AI business analyst assistant. Your main objective is to produce comprehensive, insightful, impartial, and systematically structured business reports based on provided business data, market trends, and strategic analysis.",
        "Computer Security Analyst Agent": "You are an AI specializing in computer security analysis. Your principal duty is to generate comprehensive, meticulously detailed, impartial, and systematically structured reports on computer security topics. This includes Exploits, Techniques, Threat Actors, and Advanced Persistent Threat (APT) Groups. All produced reports should adhere to the highest standards of scholarly work and provide in-depth insights into the complexities of computer security.",
        "Default Agent": "You are an AI critical thinker research assistant. Your sole purpose is to write well written, critically acclaimed, objective and structured reports on given text."
    }

    return prompts.get(agent, "No such agent")


def generate_report_prompt(question, research_summary, report_format="apa"):
    """ Generates the report prompt for the given question and research summary.
    Args: question (str): The question to generate the report prompt for
            research_summary (str): The research summary to generate the report prompt for
    Returns: str: The report prompt for the given question and research summary
    """

    return f'Information: """{research_summary}"""\n\n' \
           f'Using the above information, answer the following'\
           f' question or topic: "{question}" in a detailed report --'\
           " The report should focus on the answer to the question, should be well structured, informative," \
           " in depth, with facts and numbers if available and a minimum of 1,200 words.\n" \
           "You should strive to write the report as long as you can using all relevant and necessary information provided.\n" \
           "You must write the report with markdown syntax.\n "\
            "You MUST determine your own concrete and valid opinion based on the given information. Do NOT deter to general and meaningless conclusions.\n" \
           f"Write all used source urls at the end of the report, and make sure to not add duplicated sources, but only one reference for each.\n" \
           f"You must write the report in {report_format} format.\n " \
            f"Please do your best, this is very important to my career. "\
           f"Assume that the current date is {datetime.now().strftime('%B %d, %Y')}"

def generate_search_queries_prompt(question):
    """ Generates the search queries prompt for the given question.
    Args: question (str): The question to generate the search queries prompt for
    Returns: str: The search queries prompt for the given question
    """
    num_search_queries = Config().num_search_queries
    queries = [f'query {i+1}' for i in range(num_search_queries)]
    queries_str = ', '.join(queries)
    return f'Write {num_search_queries} google search queries to search online that form an objective opinion from the following: "{question}"'\
           f'You must respond only with a list of strings in the following json format: {queries_str}'

def generate_devops_report(research_summary, project_name):
    return f'''
    {research_summary}

    Based on the provided information, research and create an in-depth DevOps report for the "{project_name}" initiative. This report will delve into the principles, practices, and benefits of implementing DevOps within an organization. The report aims to provide comprehensive insights to guide stakeholders in understanding and adopting DevOps effectively.

    **Introduction to DevOps:**
    The report opens with an introduction to DevOps, explaining its significance as a cultural and technical movement that bridges the gap between software development and IT operations.

    **Core Principles of DevOps:**
    Detail the core principles of DevOps, emphasizing collaboration, automation, continuous integration, and continuous delivery.

    **Benefits of DevOps Implementation:**
    Discuss the advantages that adopting a DevOps approach brings, including faster time-to-market, improved quality, enhanced collaboration, and business agility.

    **DevOps Practices and Tools:**
    Elaborate on various DevOps practices and tools, such as version control, infrastructure as code (IaC), continuous integration/continuous delivery (CI/CD) pipelines, and monitoring.

    **Challenges and Considerations:**
    Address potential challenges in DevOps adoption, including cultural shifts, automation complexities, and security concerns.

    **Real-world Case Studies:**
    Highlight successful DevOps implementation case studies, showcasing how organizations have benefited from this approach.

    **Creating a DevOps Culture:**
    Discuss how to cultivate a DevOps culture, focusing on collaboration, shared responsibility, and cross-functional teams.

    **Continuous Improvement:**
    Explain the concept of continuous improvement in DevOps, emphasizing the importance of feedback loops and data-driven decision-making.

    **Best Practices for DevOps:**
    Provide actionable best practices for effective DevOps implementation, covering areas like automation, monitoring, and communication.

    **Structuring the Report:**
    Guide readers on how the report is organized, including section titles, subsections, and their significance in conveying the information effectively.

    **Documentation and Presentation:**
    Address the importance of well-structured documentation, readability, and presentation. Emphasize the use of diagrams, charts, and visual aids.

    **References and Sources:**
    List all references and sources used in the report in APA format to acknowledge the original creators and facilitate further exploration.

    **Meeting Word Count:**
    Ensure that the report meets the specified minimum length of 1,200 words, providing detailed insights while maintaining conciseness.

    **Empowering with DevOps Knowledge:**
    The DevOps report should empower stakeholders with a comprehensive understanding of DevOps principles, practices, and benefits.

    By following this structured report, readers will gain the necessary knowledge to effectively implement DevOps principles within their organization.
    '''
def generate_specialized_report(research_summary, project_name, section_titles, tag_name):
    report_content = f'''
    [{tag_name}]
    
    {research_summary}
    
    Based on the provided information, research and implement a comprehensive report for the "{project_name}" project. The report covers various aspects of the project, providing clear instructions, explanations, and best practices.
    
    **{section_titles[0]}**
    {research_summary}  # Your content for the first section
    
    **{section_titles[1]}**
    {research_summary}  # Your content for the second section
    
    ...  # Repeat for other sections
    
    Write all source URLs at the end of the report in APA format. The report should have a minimum length of 1,200 words and follow Markdown syntax and APA format.
    '''

    return report_content
    # Call the function and store the generated report in a variable
    report_content = generate_devops_report(research_summary, project_name)

    # Print or manipulate the report content as needed
    print(report_content)


def generate_readme_report_prompt(project_name, research_summary):
    """
    Generates the README.md report prompt for the given project and research summary.

    Args:
        project_name (str): The name of the project to generate the report prompt for.
        research_summary (str): The research summary to generate the report prompt for.

    Returns:
        str: The README.md report prompt for the given project and research summary.
    """


    return f'"""{research_summary}""" Based on the provided information, research and implement a comprehensive README.md'\
           f' guide for the "{project_name}" project. The guide should provide clear instructions on how to set up'\
           f' the project, including installation steps, dependencies, and configuration details. Include information'\
           f' on project structure, file organization, and usage examples. Provide explanations of key concepts,'\
           f' features, and functionality. Consider best practices for documentation and readability. Ensure that the'\
           f' guide is well-structured, informative, and follows appropriate formatting (Markdown syntax). Write all'\
           f' source URLs at the end of the guide in APA format. The guide should have a minimum length of 1,200 words'\
           f' and with Markdown syntax and APA format.'

def generate_property_management_report_prompt(property_name, management_summary):
    """
    Generates the property management report prompt for the given property and management summary.

    Args:
        property_name (str): The name of the property to generate the report prompt for.
        management_summary (str): The management summary to generate the report prompt for.

    Returns:
        str: The property management report prompt for the given property and management summary.
    """
    
    return f'"""{management_summary}""" Based on the provided information, create a comprehensive property management report for the'\
           f' property "{property_name}". The report should outline the property management activities carried out, including'\
           f' rent collection, maintenance and repairs, tenant communication, lease agreements, and tenant turnover processes.'\
           f' Describe any challenges faced during property management and how they were addressed. Highlight successful'\
           f' strategies used to maintain tenant satisfaction and property value. Utilize both qualitative and quantitative data,'\
           f' such as occupancy rates, maintenance records, and tenant feedback. Ensure that the report is well-structured,'\
           f' Write all source urls at the end of the report in apa format.'\
           f' informative, and follows appropriate formatting. The report should have a minimum length of 1,200 words and with markdown syntax and apa format.'
           
def generate_network_security_assessment_prompt(network_name, research_summary):
    """
    Generates the network security assessment report prompt for the given network and research summary.

    Args:
        network_name (str): The name of the network to generate the report prompt for.
        research_summary (str): The research summary to generate the report prompt for.

    Returns:
        str: The network security assessment report prompt for the given network and research summary.
    """
    
    return f'"""{research_summary}""" Based on the provided information, perform a comprehensive network security assessment'\
           f' for the "{network_name}" network. Evaluate the network architecture, components, and configurations to'\
           f' identify potential security vulnerabilities, weaknesses, and risks. Include an analysis of potential'\
           f' attack vectors, such as unauthorized access, data breaches, and malware propagation. Provide actionable'\
           f' recommendations and best practices for enhancing the network security posture. Utilize both qualitative'\
           f' and quantitative data, such as vulnerability scans, penetration testing results, and threat intelligence.'\
           f' Ensure that the assessment report is well-structured, informative, and follows appropriate formatting.'\
           f' Write all source urls at the end of the report in apa format.'\
           f' The report should have a minimum length of 1,200 words and with markdown syntax and apa format.'

def generar_prompt_informe_denuncia(pregunta, resumen_investigacion):
    """
    Genera un prompt de informe de denuncia basado en la pregunta y el resumen de investigación proporcionados.

    Args:
        pregunta (str): La pregunta o descripción del incidente para generar el prompt del informe.
        resumen_investigacion (str): Un resumen de la investigación o detalles del incidente.

    Returns:
        str: El prompt de informe de denuncia para la pregunta y el resumen de investigación proporcionados.
    """
    return f'Reporte el incidente descrito en la siguiente pregunta: "{pregunta}". '\
           f'Basándose en el resumen de investigación proporcionado, realice una investigación exhaustiva para recopilar toda la información disponible sobre el incidente. '\
           f'Incluya detalles como la fecha del incidente, la ubicación, las personas involucradas, las acciones tomadas y cualquier testigo. '\
           f'Mencione las pérdidas económicas sufridas, describiendo las cantidades y los elementos perdidos, si corresponde. '\
           f'Además, detalle cualquier perjuicio, ya sea físico o emocional, que haya experimentado como resultado del incidente. '\
           f'El informe debe estar bien estructurado y ser informativo, con una narración completa de los hechos. '\
           f'Asegúrese de que toda la información recopilada sea precisa y esté respaldada con evidencia adecuada. '\
           f'Escriba el informe en un mínimo de 1,200 palabras utilizando formato de markdown y APA. '\
           f'Incluya todos los URL y referencias utilizados en formato APA al final del informe.'

def generate_phone_number_report_prompt(question, research_summary):
    """
    Generates the phone number report prompt for the given question and research summary.

    Args:
        question (str): The question to generate the report prompt for.
        research_summary (str): The research summary to generate the report prompt for.

    Returns:
        str: The phone number report prompt for the given question and research summary.
    """
    return f'Based on the provided phone number "{question}", conduct a comprehensive search to gather all available information. '\
           f'Your objective is to investigate the phone number for potential associations with criminal activities. '\
           f'Include details such as the owner\'s name, address, email, social media profiles, and any other relevant information. '\
           f'Utilize online directories, social media platforms, public records, and any other reliable sources to gather the information. '\
           f'Pay close attention to any indications or connections that might suggest involvement in criminal behavior, such as records of arrests, court cases, or suspicious online activities. '\
           f'Evaluate the credibility of the sources and cross-reference the information to ensure its accuracy and reliability. '\
           f'The report should be well-structured, informative, and include all relevant details found during the search. '\
           f'Highlight any potential red flags or criminal associations discovered during the investigation. '\
           f'Ensure that all gathered information is accurate and up-to-date. Write the report in a minimum of 1,200 words with markdown syntax and APA format. '\
           f'Include all used URLs and references in APA format at the end of the report.'

def generate_architecture_report_prompt(software_name, research_summary):
    """
    Generates the architecture report prompt for the given software and research summary.

    Args:
        software_name (str): The name of the software to generate the architecture report prompt for.
        research_summary (str): The research summary to generate the architecture report prompt for.

    Returns:
        str: The architecture report prompt for the given software and research summary.
    """
    
    return f'"""{research_summary}""" Based on the provided information, create an in-depth software architecture report'\
           f' for the software "{software_name}". The report should cover the software\'s overall structure, components,'\
           ' modules, interactions, and design decisions. Utilize appropriate architectural diagrams and explanations'\
           ' to clearly convey the software\'s architecture. The report should also discuss considerations like'\
           ' scalability, maintainability, security, and performance. Ensure that the report is well-structured,'\
           ' informative, and follows Markdown syntax. Include relevant facts, figures, and technical details.'\
           ' Write all source urls at the end of the report in apa format.'\
           ' The report should have a minimum length of 1,200 words and with markdown syntax and apa format. '

def generate_market_analysis_report_prompt(market_name, research_summary):
    """
    Generates the market analysis report prompt for the given market and research summary.

    Args:
        market_name (str): The name of the market to generate the report prompt for.
        research_summary (str): The research summary to generate the report prompt for.

    Returns:
        str: The market analysis report prompt for the given market and research summary.
    """
    
    return f'"""{research_summary}""" Based on the provided information, create a comprehensive market analysis report for'\
           f' the "{market_name}" market. The report should delve into current market trends, competitive landscape,'\
           ' target demographics, consumer preferences, and potential growth opportunities. Utilize both qualitative'\
           ' and quantitative data to provide a thorough analysis. Consider factors such as market size, market share,'\
           ' industry challenges, and emerging technologies. Ensure that the report is well-structured, informative,'\
           ' and follows appropriate formatting. Include relevant facts, figures, charts, and graphs to support your'\
           ' Write all source urls at the end of the report in apa format.'\
           ' analysis. The report should have a minimum length of 1,200 words and with markdown syntax and apa format. '

def generate_risk_assessment_report_prompt(project_name, research_summary):
    """
    Generates the risk assessment report prompt for the given project and research summary.

    Args:
        project_name (str): The name of the project to generate the report prompt for.
        research_summary (str): The research summary to generate the report prompt for.

    Returns:
        str: The risk assessment report prompt for the given project and research summary.
    """
    
    return f'"""{research_summary}""" Based on the provided information, create a comprehensive risk assessment report for'\
           f' the "{project_name}" project. The report should identify potential risks, vulnerabilities, and threats'\
           ' that could impact the success of the project. Evaluate the potential consequences of each risk and'\
           ' propose mitigation strategies to minimize their impact. Consider factors such as technical, financial,'\
           ' operational, and external risks. Utilize both qualitative and quantitative data to support your analysis.'\
           ' Include relevant facts, figures, and examples to illustrate the identified risks. Ensure that the report'\
           ' is well-structured, informative, and follows appropriate formatting. The report should have a minimum'\
           ' Write all source urls at the end of the report in apa format.'\
           ' length of 1,200 words and with markdown syntax and apa format. '

def generate_medical_research_paper_prompt(topic, research_summary):
    """
    Generates the medical research paper prompt for the given research topic.

    Args:
        topic (str): The research topic for the research paper.
        research_summary (str): The research summary to generate the research paper prompt for.

    Returns:
        str: The medical research paper prompt for the given research topic.
    """
    
    return f'"""{research_summary}""" Based on the provided information, conduct an original medical research study on the topic'\
           f' of {topic}. Develop a clear research question, hypothesis, and methodology for your study. Collect and analyze'\
           f' relevant data, present your findings, and draw conclusions based on the results. Discuss the implications of'\
           f' your research findings for medical practice or knowledge. Ensure that the research paper is well-structured,'\
           f' adheres to scientific writing standards, and follows appropriate citation formats. The paper should have a'\
           f' Write all source urls at the end of the report in apa format.'\
           f' minimum length of 1,200 words and with markdown syntax and apa format. '
def generate_ux_report_prompt(product_name, research_summary):
    """
    Generates the user experience (UX) report prompt for the given product and research summary.

    Args:
        product_name (str): The name of the product to generate the report prompt for.
        research_summary (str): The research summary to generate the report prompt for.

    Returns:
        str: The user experience (UX) report prompt for the given product and research summary.
    """
    
    return f'"""{research_summary}""" Based on the provided information, create a comprehensive user experience (UX) report'\
           f' for the "{product_name}" product. The report should focus on assessing the usability, accessibility, and'\
           ' overall user satisfaction of the product. Evaluate user interactions, user flows, visual design, and'\
           ' navigation. Provide recommendations for improvements that enhance the user experience. Utilize both'\
           ' qualitative and quantitative data, such as user feedback, usability testing, and analytics. Include'\
           ' relevant facts, figures, and examples to support your analysis. Ensure that the report is well-structured,'\
           ' The report should have a minimum length of 1,200 words and with markdown syntax and apa format. '\
           ' Write all source urls at the end of the report in apa format.'\
           ' informative, and follows appropriate formatting. The report should have a minimum length of 1,200 words and with markdown syntax and apa format. '

                  
def generate_resource_report_prompt(question, research_summary):
    """Generates the resource report prompt for the given question and research summary.

    Args:
        question (str): The question to generate the resource report prompt for.
        research_summary (str): The research summary to generate the resource report prompt for.

    Returns:
        str: The resource report prompt for the given question and research summary.
    """
    return f'"""{research_summary}""" Based on the above information, generate a bibliography recommendation report for the following' \
           f' question or topic: "{question}". The report should provide a detailed analysis of each recommended resource,' \
           ' explaining how each source can contribute to finding answers to the research question.' \
           ' Focus on the relevance, reliability, and significance of each source.' \
           ' Ensure that the report is well-structured, informative, in-depth, and follows Markdown syntax.' \
           ' Include relevant facts, figures, and numbers whenever available.' \
           ' The report should have a minimum length of 1,200 words and with markdown syntax and apa format. '


def generate_outline_report_prompt(question, research_summary):
    """ Generates the outline report prompt for the given question and research summary.
    Args: question (str): The question to generate the outline report prompt for
            research_summary (str): The research summary to generate the outline report prompt for
    Returns: str: The outline report prompt for the given question and research summary
    """

    return f'"""{research_summary}""" Using the above information, generate an outline for a research report in Markdown syntax'\
           f' for the following question or topic: "{question}". The outline should provide a well-structured framework'\
           ' for the research report, including the main sections, subsections, and key points to be covered.' \
           ' The research report should be detailed, informative, in-depth, and a minimum of 1,200 words.' \
           ' Use appropriate Markdown syntax to format the outline and ensure readability.'

def generate_concepts_prompt(question, research_summary):
    """ Generates the concepts prompt for the given question.
    Args: question (str): The question to generate the concepts prompt for
            research_summary (str): The research summary to generate the concepts prompt for
    Returns: str: The concepts prompt for the given question
    """

    return f'"""{research_summary}""" Using the above information, generate a list of 5 main concepts to learn for a research report'\
           f' on the following question or topic: "{question}". The outline should provide a well-structured framework'\
           'You must respond with a list of strings in the following format: ["concepts 1", "concepts 2", "concepts 3", "concepts 4, concepts 5"]'


def generate_lesson_prompt(concept):
    """
    Generates the lesson prompt for the given question.
    Args:
        concept (str): The concept to generate the lesson prompt for.
    Returns:
        str: The lesson prompt for the given concept.
    """

    prompt = f'generate a comprehensive lesson about {concept} in Markdown syntax. This should include the definition'\
    f'of {concept}, its historical background and development, its applications or uses in different'\
    f'fields, and notable events or facts related to {concept}.'

    return prompt

def get_report_by_type(report_type):
    report_type_mapping = {
        'research_report': generate_report_prompt,
        'generate_readme': generate_readme_report_prompt,
        'generate_devops_report': generate_devops_report,
        'generate_phone_number_report_prompt': generate_phone_number_report_prompt,
        'informe_denuncia': generar_prompt_informe_denuncia,
        'resource_report': generate_resource_report_prompt,
        'ux_report': generate_ux_report_prompt,
        'risk_report': generate_risk_assessment_report_prompt,
        'market_report': generate_market_analysis_report_prompt,
        'architecture_report': generate_architecture_report_prompt,
        'medical_report': generate_medical_research_paper_prompt,
        'property_report': generate_property_management_report_prompt,
        'network_security_report': generate_network_security_assessment_prompt,
        'outline_report': generate_outline_report_prompt
    }
    return report_type_mapping[report_type]

def auto_agent_instructions():
    return """
        This task involves researching a given topic, regardless of its complexity or the availability of a definitive answer. The research is conducted by a specific agent, defined by its type and role, with each agent requiring distinct instructions.
        Agent
        The agent is determined by the field of the topic and the specific name of the agent that could be utilized to research the topic provided. Agents are categorized by their area of expertise, and each agent type is associated with a corresponding emoji.

        examples:
        task: "should I invest in apple stocks?"
        response: 
        {
            "agent": "💰 Finance Agent",
            "agent_role_prompt: "You are a seasoned finance analyst AI assistant. Your primary goal is to compose comprehensive, astute, impartial, and methodically arranged financial reports based on provided data and trends."
        }
        task: "could reselling sneakers become profitable?"
        response: 
        { 
            "agent":  "📈 Business Analyst Agent",
            "agent_role_prompt": "You are an experienced AI business analyst assistant. Your main objective is to produce comprehensive, insightful, impartial, and systematically structured business reports based on provided business data, market trends, and strategic analysis."
        }
        task: "what are the most interesting sites in Tel Aviv?"
        response:
        {
            "agent:  "🌍 Travel Agent",
            "agent_role_prompt": "You are a world-travelled AI tour guide assistant. Your main purpose is to draft engaging, insightful, unbiased, and well-structured travel reports on given locations, including history, attractions, and cultural insights."
        }
    """
