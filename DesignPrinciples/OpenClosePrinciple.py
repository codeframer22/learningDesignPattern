# Open Close Principle

class ServerHealthCheck:

    def authenticate(self, server):
        if server == 'server_A':
            # Write code to auth server A
            return ''
        if server == 'server_B':
            # Write code to auth server B
            return ''

    def perform_hc(self, server):
        if server == 'server_A':
            # Write code to perform hc on server A
            return ''
        if server == 'server_B':
            # Write code to perform hc on server A
            return ''

from abc import ABC, abstractmethod

class Authenticate(ABC):
    @abstractmethod
    def authenticate(self):
        pass

class PerformHealthCheck(ABC):
    @abstractmethod
    def perform_hc(self):
        pass

class ServerA(Authenticate, PerformHealthCheck):

    def authenticate(self):
        # write code to auth server A
        return auth_obj

    def perform_hc(self):
        # write code to perform hc on server A
        return hc_status


class ServerB(Authenticate, PerformHealthCheck):

    def authenticate(self):
        # write code to auth server A
        return auth_obj

    def perform_hc(self):
        # write code to perform hc on server A
        return hc_status