
from unittest.mock import MagicMock, patch
from services import research_workflow


def test_run_research_passes_inputs_to_kickoff():

    # Arrange: Prepare test data
    sample_input = {
        "product_name": "iPhone 14",
        "websites_list": "Amazon, eBay, Walmart",
        "country_name": "Egypt",
        "language": "English"
    }

    fake_crew = MagicMock()
    fake_crew.kickoff.return_value = "Research completed!"
        
    # Act: Replace the real Crew and run the workflow
    with patch(
        "services.research_workflow.Crew",
        return_value=fake_crew)as mock_crew:
    
        result = research_workflow.run_research(sample_input)
        mock_crew.assert_called_once_with(agents=[research_workflow.search_agent, research_workflow.search_engine_agent, research_workflow.scraping_agent, research_workflow.report_agent],
            tasks=[research_workflow.search_agent_task, research_workflow.search_engine_task, research_workflow.scraping_task, research_workflow.report_task],
            process=research_workflow.Process.sequential,
            verbose=True)
        # Assert: Verify expected behavior 

        fake_crew.kickoff.assert_called_once_with(inputs=sample_input)
        assert result == "Research completed!"





def test_run_research_handles_kickoff_error():
    # Arrange: Prepare test data
    sample_input = {
        "product_name": "iPhone 14",
        "websites_list": "Amazon, eBay, Walmart",
        "country_name": "Egypt",
        "language": "English"
    }

    fake_crew = MagicMock()
    fake_crew.kickoff.side_effect=Exception("KickOff Error")

    #Act
    with patch("services.research_workflow.Crew",return_value=fake_crew) as mock_crew:
        results=research_workflow.run_research(sample_input)
        mock_crew.assert_called_once_with(agents=[research_workflow.search_agent, research_workflow.search_engine_agent, research_workflow.scraping_agent, research_workflow.report_agent],
            tasks=[research_workflow.search_agent_task, research_workflow.search_engine_task, research_workflow.scraping_task, research_workflow.report_task],
            process=research_workflow.Process.sequential,
            verbose=True)
        #Assert
        fake_crew.kickoff.assert_called_once_with(inputs=sample_input)
        assert results == "Sorry, we couldn't complete your product research. Please try again."
        
