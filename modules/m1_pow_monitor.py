"""Starter file for module M1."""

import streamlit as st
import time
import requests

from api.blockchain_client import get_latest_block


def get_last_blocks(n=10):
    """Fetch last N blocks from Blockstream API"""
    url = f"https://blockstream.info/api/blocks"
    return requests.get(url).json()[:n]


def compute_block_times(blocks):
    """Compute time differences between consecutive blocks"""
    times = []
    for i in range(1, len(blocks)):
        t1 = blocks[i - 1]["timestamp"]
        t2 = blocks[i]["timestamp"]
        times.append(t1 - t2)
    return times


def render() -> None:
    """Render the M1 panel."""
    st.header("M1 - Proof of Work Monitor")

    st.markdown("""
    This module displays live Bitcoin mining data and helps understand Proof of Work.
    """)

    if st.button("Fetch latest block", key="m1_fetch"):
        with st.spinner("Fetching data..."):
            try:
                #  Latest block
                block = get_latest_block()

                st.subheader("Latest Block Info")
                st.write(f"Height: {block.get('height')}")
                st.write(f"Hash: {block.get('id')}")
                st.write(f"Difficulty: {block.get('difficulty')}")
                st.write(f"Nonce: {block.get('nonce')}")
                st.write(f"Transactions: {block.get('tx_count')}")

                #  Last blocks for analysis
                blocks = get_last_blocks(10)

                #  Compute block times
                block_times = compute_block_times(blocks)

                st.subheader("Block Time Analysis")
                st.write("Time between last blocks (seconds):")
                st.write(block_times)

                #  Average block time
                if block_times:
                    avg_time = sum(block_times) / len(block_times)
                    st.metric("Average Block Time (s)", round(avg_time, 2))

                #  Simple hash rate estimation
                difficulty = block.get("difficulty", 0)
                if avg_time > 0:
                    hash_rate = difficulty * (2**32) / avg_time
                    st.metric("Estimated Hash Rate", f"{hash_rate:.2e} hashes/sec")

                #  Chart
                st.subheader("Block Time Distribution")
                st.bar_chart(block_times)

            except Exception as exc:
                st.error(f"Error fetching data: {exc}")

    else:
        st.info("Click the button to fetch live Bitcoin data.")