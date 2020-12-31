# Minispaghetti
CRD operations for key-value date,
creates a json file in a location(usually where the package),
Stores as a json file named Datastore,
can be accessed by other scripts
automatically deletes the data in datastore if time to live is given,
multithreading can be done as far as tested,
Value can be anything. if multiple data is to be given, should be given in a list of tuple
create()-To add a key-value pair, if required
Delete()-to delete key-value pair,if exists
read()-To show the key-value pair,if exists and time is present
timedelete()-to delete if the program is running to save space and clear data that have TTL
#
