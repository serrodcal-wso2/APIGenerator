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
			},
			{
				"methods" : [
					"PUT"
				],
				"urlPath": "/resource3/{id}",
				"endpoint" : "conf:/Endpoints/ExampleEndpoint2" 
			}
		]
	}

## XML file obtained
	
	<api name="Test.API.Example" context="/test/example/v1">
	    <resource methods="GET POST" uri-template="/resource1">
	      <inSequence>
	      	<log category="DEBUG">
	      		<property name="*** INSIDE" value="[API] /test/example/v1/resource1"/>
	      	</log>
	        <send>
	          <endpoint uri="http://example.com" />
	        </send>
	      </inSequence>
	      <outSequence>
	      	<log category="DEBUG">
	      		<property name="*** OUTSIDE" value="[API] /test/example/v1/resource1"/>
	      	</log>
	        <send />
	      </outSequence>
	      <faultSequence />
	    </resource>
	    <resource methods="POST" uri-template="/resource2">
	      <inSequence>
	      	<log category="DEBUG">
	      		<property name="*** INSIDE" value="[API] /test/example/v1/resource2"/>
	      	</log>
	        <send>
	          <endpoint key="conf:/Endpoints/ExampleEndpoint" />
	        </send>
	      </inSequence>
	      <outSequence>
	      	<log category="DEBUG">
	      		<property name="*** OUTSIDE" value="[API] /test/example/v1/resource2"/>
	      	</log>
	        <send />
	      </outSequence>
	      <faultSequence />
	    </resource>
	    <resource methods="PUT" uri-template="/resource3/{id}">
		    <inSequence>
		      <log category="DEBUG">
		        <property name="*** INSIDE" value="[API]/test/example/v1/resource3/{id} "/>
		      </log>
		      <send>
		        <endpoint key="conf:/Endpoints/ExampleEndpoint2" />
		      </send>
		    </inSequence>
		    <outSequence>
		      <log category="DEBUG">
		        <property name="*** INSIDE" value="[API]/test/example/v1/resource3/{id} "/>
		      </log>
		      <send />
		    <outSequence>
		    <faultSequence/>
		</resource>
	</api>