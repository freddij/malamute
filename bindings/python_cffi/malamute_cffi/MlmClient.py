################################################################################
#  THIS FILE IS 100% GENERATED BY ZPROJECT; DO NOT EDIT EXCEPT EXPERIMENTALLY  #
#  Read the zproject/README.md for information about making permanent changes. #
################################################################################
from . import utils
from . import destructors
libmalamute_destructors = destructors.lib

class MlmClient(object):
    """
    Malamute Client

    Codec class for mlm_client.
    """

    def __init__(self):
        """
        Create a new mlm_client, return the reference if successful,
        or NULL if construction failed due to lack of available memory.
        """
        p = utils.lib.mlm_client_new()
        if p == utils.ffi.NULL:
            raise MemoryError("Could not allocate person")

        # ffi.gc returns a copy of the cdata object which will have the
        # destructor called when the Python object is GC'd:
        # https://cffi.readthedocs.org/en/latest/using.html#ffi-interface
        self._p = utils.ffi.gc(p, libmalamute_destructors.mlm_client_destroy_py)

    def actor(self):
        """
        Return actor, when caller wants to work with multiple actors and/or
        input sockets asynchronously.
        """
        return utils.lib.mlm_client_actor(self._p)

    def msgpipe(self):
        """
        Return message pipe for asynchronous message I/O. In the high-volume case,
        we send methods and get replies to the actor, in a synchronous manner, and
        we send/recv high volume message data to a second pipe, the msgpipe. In
        the low-volume case we can do everything over the actor pipe, if traffic
        is never ambiguous.
        """
        return utils.lib.mlm_client_msgpipe(self._p)

    def connected(self):
        """
        Return true if client is currently connected, else false. Note that the
        client will automatically re-connect if the server dies and restarts after
        a successful first connection.
        """
        return utils.lib.mlm_client_connected(self._p)

    def set_plain_auth(self, username, password):
        """
        Set PLAIN authentication username and password. If you do not call this, the
        client will use NULL authentication. TODO: add "set curve auth".
        Returns >= 0 if successful, -1 if interrupted.
        """
        return utils.lib.mlm_client_set_plain_auth(self._p, utils.to_bytes(username), utils.to_bytes(password))

    def connect(self, endpoint, timeout, address):
        """
        Connect to server endpoint, with specified timeout in msecs (zero means wait
        forever). Constructor succeeds if connection is successful. The caller may
        specify its address.
        Returns >= 0 if successful, -1 if interrupted.
        """
        return utils.lib.mlm_client_connect(self._p, utils.to_bytes(endpoint), timeout, utils.to_bytes(address))

    def set_producer(self, stream):
        """
        Prepare to publish to a specified stream. After this, all messages are sent to
        this stream exclusively.
        Returns >= 0 if successful, -1 if interrupted.
        """
        return utils.lib.mlm_client_set_producer(self._p, utils.to_bytes(stream))

    def set_consumer(self, stream, pattern):
        """
        Consume messages with matching subjects. The pattern is a regular expression
        using the CZMQ zrex syntax. The most useful elements are: ^ and $ to match the
        start and end, . to match any character, \s and \S to match whitespace and
        non-whitespace, \d and \D to match a digit and non-digit, \a and \A to match
        alphabetic and non-alphabetic, \w and \W to match alphanumeric and
        non-alphanumeric, + for one or more repetitions, * for zero or more repetitions,
        and ( ) to create groups. Returns 0 if subscription was successful, else -1.
        Returns >= 0 if successful, -1 if interrupted.
        """
        return utils.lib.mlm_client_set_consumer(self._p, utils.to_bytes(stream), utils.to_bytes(pattern))

    def remove_consumer(self, stream):
        """
        Remove all subscriptions to a stream
        Returns >= 0 if successful, -1 if interrupted.
        """
        return utils.lib.mlm_client_remove_consumer(self._p, utils.to_bytes(stream))

    def set_worker(self, address, pattern):
        """
        Offer a particular named service, where the pattern matches request subjects
        using the CZMQ zrex syntax.
        Returns >= 0 if successful, -1 if interrupted.
        """
        return utils.lib.mlm_client_set_worker(self._p, utils.to_bytes(address), utils.to_bytes(pattern))

    def send(self, subject, content):
        """
        Send STREAM SEND message to server, takes ownership of message
        and destroys message when done sending it.
        """
        return utils.lib.mlm_client_send(self._p, utils.to_bytes(subject), utils.ffi.new("zmsg_t **", content._p))

    def sendto(self, address, subject, tracker, timeout, content):
        """
        Send MAILBOX SEND message to server, takes ownership of message
        and destroys message when done sending it.
        """
        return utils.lib.mlm_client_sendto(self._p, utils.to_bytes(address), utils.to_bytes(subject), utils.to_bytes(tracker), timeout, utils.ffi.new("zmsg_t **", content._p))

    def sendfor(self, address, subject, tracker, timeout, content):
        """
        Send SERVICE SEND message to server, takes ownership of message
        and destroys message when done sending it.
        """
        return utils.lib.mlm_client_sendfor(self._p, utils.to_bytes(address), utils.to_bytes(subject), utils.to_bytes(tracker), timeout, utils.ffi.new("zmsg_t **", content._p))

    def recv(self):
        """
        Receive message from server; caller destroys message when done
        """
        return utils.lib.mlm_client_recv(self._p)

    def command(self):
        """
        Return last received command. Can be one of these values:
            "STREAM DELIVER"
            "MAILBOX DELIVER"
            "SERVICE DELIVER"
        """
        return utils.lib.mlm_client_command(self._p)

    def status(self):
        """
        Return last received status
        """
        return utils.lib.mlm_client_status(self._p)

    def reason(self):
        """
        Return last received reason
        """
        return utils.lib.mlm_client_reason(self._p)

    def address(self):
        """
        Return last received address
        """
        return utils.lib.mlm_client_address(self._p)

    def sender(self):
        """
        Return last received sender
        """
        return utils.lib.mlm_client_sender(self._p)

    def subject(self):
        """
        Return last received subject
        """
        return utils.lib.mlm_client_subject(self._p)

    def content(self):
        """
        Return last received content
        """
        return utils.lib.mlm_client_content(self._p)

    def tracker(self):
        """
        Return last received tracker
        """
        return utils.lib.mlm_client_tracker(self._p)

    def sendx(self, subject, content, *content_args):
        """
        Send multipart string message to stream, end list with NULL
        Returns 0 if OK, -1 if failed due to lack of memory or other error.
        """
        return utils.lib.mlm_client_sendx(self._p, utils.to_bytes(subject), utils.to_bytes(content), *content_args)

    def sendtox(self, address, subject, content, *content_args):
        """
        Send multipart string to mailbox, end list with NULL
        Returns 0 if OK, -1 if failed due to lack of memory or other error.
        """
        return utils.lib.mlm_client_sendtox(self._p, utils.to_bytes(address), utils.to_bytes(subject), utils.to_bytes(content), *content_args)

    def sendforx(self, address, subject, content, *content_args):
        """
        Send multipart string to service, end list with NULL
        Returns 0 if OK, -1 if failed due to lack of memory or other error.
        """
        return utils.lib.mlm_client_sendforx(self._p, utils.to_bytes(address), utils.to_bytes(subject), utils.to_bytes(content), *content_args)

    def recvx(self, subject_p, string_p, *string_p_args):
        """
        Receive a subject and string content from the server. The content may be
        1 or more string frames. This method is orthogonal to the sendx methods.
        End the string arguments with NULL. If there are not enough frames in
        the received message, remaining strings are set to NULL. Returns number
        of string contents received, or -1 in case of error. Free the returned
        subject and content strings when finished with them. To get the type of
        the command, use mlm_client_command ().
        """
        return utils.lib.mlm_client_recvx(self._p, utils.to_bytes(subject_p), utils.to_bytes(string_p), *string_p_args)

    def set_verbose(self, verbose):
        """
        Enable verbose tracing (animation) of state machine activity.
        """
        utils.lib.mlm_client_set_verbose(self._p, verbose)

    @staticmethod
    def test(verbose):
        """
        Self test of this class.
        """
        utils.lib.mlm_client_test(verbose)

################################################################################
#  THIS FILE IS 100% GENERATED BY ZPROJECT; DO NOT EDIT EXCEPT EXPERIMENTALLY  #
#  Read the zproject/README.md for information about making permanent changes. #
################################################################################
