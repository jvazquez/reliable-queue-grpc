# Reliable queue grpc

A proof of concept using a reliable queue and a grpc client / server


# Concept

We will generate a random number and we will place the number in the
grpc client.
The server will place the number in the reliable queue.
The reliable queue will deliver to a worker the number.
The worker will calculate the fibonacci of the provided number.
We need to deliver a response based of this number.

# Worker.

I'm fooling around with Fibonacci, so I'll be using different solutions, recursion,
generators, Binet.
Instead of using a time.sleep to simulate a long running operation, I produce that
so it's much more interesting.
The purpose is to simulate I/O with long running tasks