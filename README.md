# APIGenerator

Script to create API definition for WSO2 ESB

	~$ python apig.py "example.json"

## JSON Example

	{
		"apiName" : "Test.API.Example",
		"apiContext" : "/test/example/v1",
		"resources" : [
			{
				"methods" : [
					"GET",
					"POST"
				],
				"urlPath": "/resource1",
				"endpoint" : "http://example.com"
			},
			{
				"methods" : [
					"POST"
				],
				"urlPath": "/resource2",
				"endpoint" : "conf:/Endpoints/ExampleEndpoint" 
			}
		]
	}

## XML file obtained
	
	<api name="Test.API.Example" context="/test/example/v1">
	    <resource methods="GET POST" uri-template="/resource1">
	      <inSequence>
	        <send>
	          <endpoint uri="http://example.com" />
	        </send>
	      </inSequence>
	      <outSequence>
	         <send />
	      </outSequence>
	      <faultSequence />
	    </resource>
	    <resource methods="POST" uri-template="/resource1">
	      <inSequence>
	        <send>
	          <endpoint key="conf:/Endpoints/ExampleEndpoint" />
	        </send>
	      </inSequence>
	      <outSequence>
	         <send />
	      </outSequence>
	      <faultSequence />
	    </resource>
	</api>