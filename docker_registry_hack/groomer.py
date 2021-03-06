# Copyright (C) 2018 BROADSoftware
#
# This file is part of EzCluster
#
# EzCluster is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# EzCluster is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with EzCluster.  If not, see <http://www.gnu.org/licenses/lgpl-3.0.html>.


from misc import setDefaultInMap,resolveDns

CLUSTER = "cluster"
DOCKER_REGISTRY_HACK = "docker_registry_hack"
DISABLED = "disabled"
ALIASES = "aliases"
ETC_HOST_ENTRIES = "etc_hosts_entries"
TARGET_IP = "target_ip"


def groom(_plugin, model):
    setDefaultInMap(model[CLUSTER][DOCKER_REGISTRY_HACK], DISABLED, False)
    if model[CLUSTER][DOCKER_REGISTRY_HACK][DISABLED]:
        return False
    else:
        if ETC_HOST_ENTRIES in model[CLUSTER][DOCKER_REGISTRY_HACK]:
            for entry in model[CLUSTER][DOCKER_REGISTRY_HACK][ETC_HOST_ENTRIES]:
                entry[TARGET_IP] = resolveDns(entry[TARGET_IP])
                if ALIASES not in entry:
                    entry[ALIASES] = "quay.io gcr.io k8s.gcr.io registry-1.docker.io"
        return True
    



