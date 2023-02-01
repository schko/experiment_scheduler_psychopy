from __future__ import annotations

from typing import List, Optional, Sequence, Tuple

from .. import frames
from ..typing import ExtensionName, ExtensionParameter


__all__ = ["Extension", "ClientExtensionFactory", "ServerExtensionFactory"]


class Extension:
    """
    Base class for extensions.

    """

    name: ExtensionName
    """Extension identifier."""

    def decode(
        self,
        frame: frames.Frame,
        *,
        max_size: Optional[int] = None,
    ) -> frames.Frame:
        """
        Decode an incoming frame.

        Args:
            frame (Frame): incoming frame.
            max_size: maximum payload size in bytes.

        Returns:
            Frame: Decoded frame.

        Raises:
            PayloadTooBig: if decoding the payload exceeds ``max_size``.

        """

    def encode(self, frame: frames.Frame) -> frames.Frame:
        """
        Encode an outgoing frame.

        Args:
            frame (Frame): outgoing frame.

        Returns:
            Frame: Encoded frame.

        """


class ClientExtensionFactory:
    """
    Base class for client-side extension factories.

    """

    name: ExtensionName
    """Extension identifier."""

    def get_request_params(self) -> List[ExtensionParameter]:
        """
        Build parameters to send to the server for this extension.

        Returns:
            List[ExtensionParameter]: Parameters to send to the server.

        """

    def process_response_params(
        self,
        params: Sequence[ExtensionParameter],
        accepted_extensions: Sequence[Extension],
    ) -> Extension:
        """
        Process parameters received from the server.

        Args:
            params (Sequence[ExtensionParameter]): parameters received from
                the server for this extension.
            accepted_extensions (Sequence[Extension]): list of previously
                accepted extensions.

        Returns:
            Extension: An extension instance.

        Raises:
            NegotiationError: if parameters aren't acceptable.

        """


class ServerExtensionFactory:
    """
    Base class for server-side extension factories.

    """

    name: ExtensionName
    """Extension identifier."""

    def process_request_params(
        self,
        params: Sequence[ExtensionParameter],
        accepted_extensions: Sequence[Extension],
    ) -> Tuple[List[ExtensionParameter], Extension]:
        """
        Process parameters received from the client.

        Args:
            params (Sequence[ExtensionParameter]): parameters received from
                the client for this extension.
            accepted_extensions (Sequence[Extension]): list of previously
                accepted extensions.

        Returns:
            Tuple[List[ExtensionParameter], Extension]: To accept the offer,
            parameters to send to the client for this extension and an
            extension instance.

        Raises:
            NegotiationError: to reject the offer, if parameters received from
                the client aren't acceptable.

        """
