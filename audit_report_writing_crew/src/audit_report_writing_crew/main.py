#!/usr/bin/env python
import sys
import warnings

from crew import AuditReportWritingCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """

    #finding_condition = input("What is the audit finding condition? ")
    #finding_criteria = input("What is the audit finding criteria? ")    
    #finding_rca = input("What is the audit finding root cause analysis? ")
    #finding_risk = input("What is the audit finding risk? ")
    #finding_management_action = input("What is the audit finding management action? ")

    finding_condition = "The audit finding condition is that company employees not protecting confidential information and use unauthorized access to the systems."
    finding_criteria = "The audit finding criteria is Central Bank regulation no 123 enforce confidential information protection and to have system access approved and authorized."
    finding_rca = "The audit finding root cause analysis is that the company has not implemented a proper data security policy in line with central bank regulation no 123."
    finding_risk = "The audit finding risk is that the company is exposed to compliance violation and penalties."
    finding_management_action = "The audit finding management action is that the company has to implement and enforce a security policy that fulfills the central bank regulatory requirements no 123."
    
    inputs = {
        'finding_condition': finding_condition,
        'finding_criteria': finding_criteria,
        'finding_rca': finding_rca,
        'finding_risk': finding_risk,
        'finding_management_action': finding_management_action
    }
    AuditReportWritingCrew().crew().kickoff(inputs=inputs)


run()