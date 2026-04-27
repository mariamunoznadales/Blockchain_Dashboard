"""Ethereum adapter backed by live public RPC data."""
from __future__ import annotations

import streamlit as st

from adapters.base import AssetIdentity, ModuleSpec, TopMetric
from api.ethereum_client import latest_block_snapshot
from modules.eth_live import (
    render_evolution,
    render_forecast,
    render_mechanism,
    render_state,
)


@st.cache_data(ttl=30, show_spinner=False)
def _cached_top_metrics(asset_code: str = "ETH") -> list[TopMetric]:
    snapshot = latest_block_snapshot(asset_code)
    return [
        TopMetric("Block Height", f"{snapshot['block_number']:,}"),
        TopMetric("Base Fee", f"{snapshot['base_fee_gwei']:,.2f} gwei"),
        TopMetric("Gas Used", f"{snapshot['gas_ratio'] * 100:,.1f}%"),
        TopMetric("Block Time", f"{snapshot['block_time']:.1f} s" if snapshot["block_time"] else "—"),
    ]


IDENTITY = AssetIdentity(
    code="ETH",
    name="Ethereum",
    symbol="ETH",
    kicker="ETHEREUM SMART CONTRACT LAYER",
    accent="#627EEA",
    accent_soft="#B794F4",
    available=True,
)


class EthAdapter:
    identity = IDENTITY
    state_renderer = staticmethod(render_state)
    mechanism_renderer = staticmethod(render_mechanism)
    evolution_renderer = staticmethod(render_evolution)
    forecast_renderer = staticmethod(render_forecast)

    def top_metrics(self) -> list[TopMetric]:
        try:
            return _cached_top_metrics("ETH")
        except Exception:
            return [
                TopMetric("Block Height", "—"),
                TopMetric("Base Fee", "—"),
                TopMetric("Gas Used", "—"),
                TopMetric("Block Time", "—"),
            ]

    def state_module(self) -> ModuleSpec:
        return ModuleSpec(
            panel_label="State | Current Network State",
            title="Network Activity",
            caption="Live Ethereum block demand.",
        )

    def mechanism_module(self) -> ModuleSpec:
        return ModuleSpec(
            panel_label="Mechanism | How The Block Is Built",
            title="Block Structure",
            caption="Slot, gas and base fee breakdown.",
        )

    def evolution_module(self) -> ModuleSpec:
        return ModuleSpec(
            panel_label="Evolution | Fees Through Time",
            title="Base Fee History",
            caption="EIP-1559 fee evolution.",
        )

    def forecast_module(self) -> ModuleSpec:
        return ModuleSpec(
            panel_label="Decision | Congestion Outlook",
            title="Gas Forecast",
            caption="Next-block fee expectation.",
        )

    def warm_cache(self) -> None:
        latest_block_snapshot("ETH")
        _cached_top_metrics("ETH")
