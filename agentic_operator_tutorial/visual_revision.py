"""Plain language throughout, with visual explanations for the teaching concepts."""
from pathlib import Path
from copy import deepcopy
import json
ROOT=Path(__file__).resolve().parent

def revise(slides):
    wording={}
    for name in ('plain_language_1.json','plain_language_2.json'):
        wording.update(json.loads((ROOT/name).read_text(encoding='utf-8')))
    keys=[item['title'] for item in slides]
    assert set(keys)==set(wording), 'Every slide needs a plain-language review'
    items={key:deepcopy(item) for key,item in zip(keys,slides)}
    for key,item in items.items():item.update(wording[key])

    def diagram(key,stem,points,caption,title=None):
        item=items[key]
        item.update(kind='diagram',diagram=stem,image=None,image2=None,excerpt=[],
                    math_tex='',math_html='',callout='',points=points,caption=caption,
                    visual_height_cm=3.8,visual_height_px=315)
        if title:item['title']=title

    diagram('What is agentic AI?','va_system_overview',[
        'An agentic system uses feedback to choose and adjust actions toward a goal.',
        'The full process can combine tools, working context and checks. One agent may be enough.'],
        'One illustrative power-study process. This is a working definition, not a universal architecture.')

    # Replace the former route-preview slide, keeping the same 80-slide teaching time.
    gen_key='The engineering question behind the news'
    gen=items[gen_key]
    gen.update(title='Generative AI creates content',kind='diagram',diagram='va_generation_call',
        image=None,image2=None,excerpt=[],math_tex='',math_html='',callout='',eyebrow='',
        refs=['GEN01','DEF03'],main_ref='GEN01',points=[
            'Generative AI makes text, images and other content. Large language models (LLMs) are used for text.',
            'A single call can create a draft. An agent system can use the same model to choose steps.'],
        caption='Illustrative report-drafting example. Generative models can also be components of agents.',
        visual_height_cm=3.8,visual_height_px=315,
        note='NIST AI 600-1 describes generative AI in terms of producing synthetic content, including text, images, audio and other media. This diagram shows one generation call: selected records and a request enter a model, which produces a draft. It does not say every generative-AI application is a single call. An LLM-based agent can use a generative model inside a repeated decision process. These categories describe different roles, not three mutually exclusive technologies or stages of a historical evolution. Generated wording is not itself numerical grid evidence; a study report should cite the engineering records used.')

    diagram('What is an AI agent?','va_classical_agent',[
        'An agent observes an environment and chooses actions that affect it.',
        'In a study, an engineering solver calculates grid behavior. The agent reads its results and chooses the next tool call.'],
        'The classical agent idea is broader than LLMs. The decision rule can use many kinds of software.')
    items['What is an AI agent?']['note']+=' Teaching notation: a_t = pi(o_1, ..., o_t), a rule mapping past observations to the next action.'

    diagram('Workflow and agent: who directs the next step?','va_workflow_agent',[
        'In a fixed workflow, code sets the steps and branches.',
        'In an LLM agent, the model chooses some next steps from the allowed actions, using the results so far.'],
        'A simplified comparison using Anthropic’s terms. A loop by itself does not make a process an agent.')

    diagram('Agency is relative to a goal and an operating boundary','va_authority',[
        'The agent can run agreed studies and prepare a report with evidence.',
        'The operator reviews the findings and decides whether an operating action is allowed.'],
        'Illustrative authority boundary for this tutorial. Running a study does not grant permission to control equipment.')
    items['Agency is relative to a goal and an operating boundary']['note']=(
        'This is an illustrative advisory-study policy informed by classical work on agency. '
        'Wooldridge and Jennings discuss autonomy, response to change, initiative and interaction; '
        'they do not prescribe this grid-operator approval process. '
        'The example gives the agent permission to run agreed studies and prepare evidence. '
        'The operator can request changes, stop the process or approve a later operating action. '
        'This diagram does not give the agent direct control of physical equipment.')

    # Original published concept diagrams, displayed with only empty margins trimmed.
    framework=items['Framework, platform and application identify different roles']
    framework.update(kind='figure',diagram=None,image='source_anthropic_augmented_llm_wide.svg',image2=None,
        excerpt=[],math_tex='',math_html='',callout='',title='A model can use records, tools and memory',
        points=['Retrieval finds records; tools run tasks; memory keeps useful context.',
                'LangGraph can manage the steps. PowerAgent supplies power-domain components; PowerDAG is one specific system.'],
        caption='Original Anthropic building-block figure. It is a general pattern, not a diagram of PowerAgent or PowerDAG.',
        refs=['DEF03','DEF04','PA02','PD01'],main_ref='DEF03',visual_height_cm=4.05,visual_height_px=350)
    framework['note']+=' The published figure shows an augmented language model. Retrieval, tools and memory are supporting capabilities; they are not mandatory in every agent. The diagram is reproduced from Anthropic with only empty margins trimmed in the display. The original image bytes are retained.'

    loop=items['An agent chooses calls; tools produce observations']
    loop.update(kind='figure',diagram=None,image='source_anthropic_autonomous_agent_wide.svg',image2=None,
        excerpt=[],math_tex='',math_html='',callout='',title='An LLM agent acts, reads the result and decides again',
        points=['After an action, the agent reads what happened before choosing the next step.',
                'It can call another allowed tool, ask a person or stop. An error is also useful feedback.'],
        caption='Original Anthropic agent-loop figure. In a grid study, feedback can be solver results or a failed check.',
        refs=['DEF03','LG01','E01'],main_ref='DEF03',visual_height_cm=4.05,visual_height_px=350)
    loop['note']+=' This is the original published conceptual agent pattern, not a measured utility or PowerAgent implementation. The display trims only empty margins. Feedback does not automatically mean model weights are being retrained.'

    diagram('PowerAgent example: study the impact of added load','va_powerwf',[
        'It runs power flow and single-outage checks (N−1) for the original case and the added-load case.',
        'LangGraph manages the steps and saved results. PowerWorld calculates the electrical results.'],
        'Simplified view of one PowerWF source-code example, not every component of the PowerAgent platform.')
    diagram('DrAgent: a plan connects domain-specific tools','va_dragent',[
        'The plan chooses signal-analysis tools or manual search to match the question.',
        'Signal tools measure the fault. Manual search finds product information in documents.'],
        'Teaching view of DrAgent. Dashed paths are used for relevant manual questions, not for every fault calculation.',
        title='DrAgent selects tools to answer a fault question')
    diagram('Three graphs describe different parts of the study','va_three_graphs',[
        'Grid edges show electrical connections. A task DAG (directed acyclic graph) links calculations through the results they need.',
        'Workflow edges show which software step can run next, including a retry loop.'],
        'Three different meanings of “graph.” These small examples explain connections, not calculated electrical results.')
    items['A DAG exposes the prerequisites of a calculation']['points']=[
        'A DAG links results to calculations that need them. Its arrows do not form a loop.',
        'Run independent calculations when inputs are ready. Wait for every required result before reporting.']
    items['A checkpoint preserves state across a pause']['points']=[
        'A checkpoint saves progress; thread_id links the saved steps to the same workflow.',
        'Changed grid connections can make old results invalid. Check them and rerun affected studies.']
    items['A retrieved instruction must remain untrusted data']['points']=[
        'Treat instructions inside a retrieved document as data, not permission.',
        'The application checks who may act and which actions are allowed.']
    items['NYPA: agentic AI discussion and the data foundation']['points'][1]=(
        'A separate demo uses the Model Context Protocol (MCP) to connect Genie to Ataccama’s data-quality check.')
    items['PowerDAG: what is reproducible and what transfers?']['points'][1]=(
        'Three task groups can run with the public files. Seven need private grid-map data and network tools.')
    items['PowerDAG: supervise a distribution-grid tool workflow']['excerpt'][2]='check earlier tools that change the study state'
    items['PowerDAG result: a controlled workflow comparison']['points'][1]=(
        'Pass@1 measures first-run workflow success: required tool calls, valid inputs and correct order. It does not measure field reliability.')
    items['PowerDAG result: a controlled workflow comparison']['caption']=(
        'PowerDAG v4, Table II. ReAct: a reason-and-act loop. JIT: prerequisite checks just before a call.')
    items['X-GridAgent result: nonconvergence remains part of the answer']['points']=[
        'The 39-bus AC optimal power flow (OPF) study solves the base and outage cases. Doubling the load does not converge.']
    items['An agent chooses actions; a tool exposes a capability']['visual_height_cm']=3.9
    framework['visual_height_cm']=3.95
    diagram('Feedback-driven simulation agents retrieve functions and options','va_simulation_feedback',[
        'The agent finds MATLAB functions and settings, writes code and runs the study.',
        'A software error triggers repair. Code that runs can still use the wrong settings.'],
        'Simplified paper workflow. Running without an error is different from meeting the requested engineering task.')
    diagram('X-GridAgent separates planning, coordination and tool actions','va_xgrid',[
        'The planner breaks down the request. The coordinator passes work to specialized tool services.',
        'Eight MCP services handle analysis, data and plots. Numerical studies use pandapower.'],
        'Architecture summary from X-GridAgent. Only numerical calls are shown going to pandapower.')
    diagram('MCP connects tools to the workflow graph','va_mcp',[
        'The client sends a named request and inputs. The server calls the available tool.',
        'MCP connects these parts. The application still checks permissions, case versions and what the results mean.'],
        'Requests and results use the client/server connection. MCP does not decide which engineering call is appropriate.')

    keys.remove(gen_key)
    keys.insert(keys.index('What is an AI agent?'),gen_key)
    result=[items[key] for key in keys]
    assert len(result)==80 and sum(item['minutes'] for item in result)==165
    assert sum(item['kind']=='exercise' for item in result)==2
    return result
